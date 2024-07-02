import csv
from models.dish import Dish
from models.order_item import OrderItem
from paths import DISH_PATH, ORDER_ITEM_PATH, ORDER_PATH, PAYMENTS_PATH, TABLES_PATH
from .order_item import STATUS_CHOICE
from .order import Order, PAYMENT_CHOICES
from update_func import update_value_in_csv



class Waiter:
    def __init__(self, user):
        from auth.create_session import get_session

        self.user = user
        self.orders = []
        self.session = get_session()
        self.permissions = {
            'Get Order': self.create_order, 
            'Add Order to Kitchen' : self.create_order,
            'Check Orders': self.check_orders,
            'Get Payment': self.get_payment,
            'Deliver Order': self.deliver_order
            }
    

    # @user.setter
    # def user(self,user):
    #     if user.role == "Waiter":
    #         self.user = user
    #     raise ValueError("This user is not a waiter")
    
    def get_dish_names(self):
        from models.dish import Dish
        dishes = []

        while True:
            dish_name = input('Dish Name>>>')
            print('When you finish input 1')
            
            dish_found = False
            if dish_name == '1':
                break
            with open(file=DISH_PATH, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['name'] == dish_name:
                        dish_found = True
                        if self.session.restourant.kitchen.check_if_enough_ingredients(dish=dish_name):

                            dish = Dish(**row)
                            dishes.append(dish)
                        else:
                            print('Not Enough Ingredients For the Dish')
                  
                if not dish_found:
                    print('Not a valid Dish')
        return dishes
    



    def get_table_id(self):
        table_found = False
        while True:
            try:
                table_id = int(input('Table id'))
                with open(file=TABLES_PATH, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        print(row['number'])
                        if int(row['number']) == table_id:
                            table_found = True
                            break

                if not table_found:
                    print('No table With that id')
                    table_id = None
                else:
                    break

            except ValueError:
                print('Input Valid Table Id')

        return table_id
    

    def create_order(self):
        dishes = self.get_dish_names()
        table_id = self.get_table_id()
        waiter = self.user
        pending_order_exists = False

        order_price = 0

        for dish in dishes:
            order_price += float(dish.price) 

        order_price += order_price / 100 * float(self.session.restourant.commision_percent)


        if dishes and table_id:
            for order in self.session.restourant.kitchen.current_orders:
                if int(order.table) == table_id and order.payement == PAYMENT_CHOICES[1]:
                    pending_order_exists = True
                    break


            orderitems = []
            dishes_names = [dish.name for dish in dishes]

            orderitems = [OrderItem(dish=dish, order_table=table_id) for dish in dishes_names]
            orderitem_ids = [orderitem.id for orderitem in orderitems]

            if not pending_order_exists:
                order = Order(table=table_id, orderitems=[], waiter=waiter, price=order_price)
                order.orderitems = orderitems
                self.orders.append(order)
                with open(file=ORDER_PATH, mode='a', encoding='utf-8') as file:
                    headers = ['table', 'dishes', 'orderitem_ids', 'waiter', 'status', 'payment', 'price']

                    writer = csv.DictWriter(file, fieldnames=headers)

                    writer.writerow({

                        'table': table_id,
                        'dishes': dishes_names,
                        'orderitem_ids': orderitem_ids,
                        'waiter': waiter.username,
                        'status': order.status,
                        'payment': order.payement,
                        'price': order.price,

                    })
   



                with open(ORDER_ITEM_PATH, 'a') as file:
                    headers = ['id', 'order', 'dish', 'status']

                    writer = csv.DictWriter(file, fieldnames=headers)
                    
                    for order_item in orderitems:
                        writer.writerow({
                            'id': order_item.id,
                            'order': order_item.order_table,
                            'dish': order_item.dish,
                            'status': order_item.status
                        })

                self.session.restourant.warehouse.write_products()

                return order
            
            print('Order Could not be placed at this Table')
            return None
        


    
    def check_orders(self):
        from auth.create_session import get_session
        orders = get_session().restourant.kitchen.current_orders
        available_orders = []
        for order in orders:
            print(order.waiter, self.session.current_user.user.username)

            if order.waiter == get_session().current_user.user.username:
                for order_item in order.orderitems:
                    if order_item.status == 'Done':
                        available_orders.append(order_item)

        print('Available Orders')
        for order in available_orders:
            print(f'Orderitem id: {order.id} OrderItem: {order.dish}, Order Status: {order.status}, Table Number: {order.order_table}')

        return available_orders
    
    
    def deliver_order(self):
        available_orders = self.check_orders()
        if available_orders:
            id = input('Which order item would you like to deliver?')
            if id.isdigit():
                for order_item in available_orders:
                    if order_item.id == id:
                        order_item.status = STATUS_CHOICE[2]
                        update_value_in_csv(
                            path=ORDER_ITEM_PATH, 
                            identifier=order_item.id, 
                            identifier_column='id', 
                            value=order_item.status, 
                            value_column='status')
                        return True

            else:
                print('Not a valid value')
                return None
            return None
    

    def get_payment(self):
        print('Tables That have not yet paid')

        if self.session.restourant.kitchen.current_orders:
            for order in self.session.restourant.kitchen.current_orders:
                if order.payement == 'Unpaid' and order.waiter == self.session.current_user.user.username:
                    print(order.table)
        
        else:
            print('No tables')
            return
        
        table_id = self.get_table_id()
        table_order = None


        for order in self.session.restourant.kitchen.current_orders:
            if int(order.table) == table_id and order.payement == PAYMENT_CHOICES[1] and order.status == 'Finished':
                table_order = order
                break
        
        if table_order:

            payment_amount = table_order.price


            with open(PAYMENTS_PATH, 'a') as file:
                writer = csv.DictWriter(file, fieldnames=['amount'])
                writer.writerow({'amount': payment_amount})
            table_order.payement = PAYMENT_CHOICES[0]


            rows = []
            with open(ORDER_PATH, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row['table'], (row['payment']))
                    if int(row['table']) == table_id and row['payment'] == PAYMENT_CHOICES[1]:
                        row['payment'] = PAYMENT_CHOICES[0]
                    rows.append(row)

            with open(ORDER_PATH, 'w', newline='') as file:
                fieldnames = rows[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)


            return sum
        print('No order found')
        return None
    

