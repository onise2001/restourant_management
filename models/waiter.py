import csv
from models.order_item import OrderItem
from paths import DISH_PATH, ORDER_ITEM_PATH, ORDER_PATH, TABLES_PATH
from .order import Order
from update_func import update_value_in_csv



class Waiter:
    def __init__(self, user):
        self.user = user
        self.orders = []
        self.permissions = {
            'Get Order': self.create_order, 
            'Add Order to Kitchen' : self.create_order,
            'Check Orders': self.check_orders
            }
    

    # @user.setter
    # def user(self,user):
    #     if user.role == "Waiter":
    #         self.user = user
    #     raise ValueError("This user is not a waiter")
    
    def get_dish_names(self):
        from models.dish import Dish
        from auth.create_session import session
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
                        if session.restourant.kitchen.check_if_enough_ingredients(dish=dish_name):
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
        from auth.create_session import session
        dishes = self.get_dish_names()
        table_id = self.get_table_id()
        waiter = self.user
        order_exists = False
        existing_order = None

        if dishes and table_id:
            for order in session.restourant.kitchen.current_orders:
                if int(order.table) == table_id:
                    order_exists = True
                    existing_order = order
                    break


            orderitems = []
            dishes_names = [dish.name for dish in dishes]

            orderitems = [OrderItem(dish=dish, order_table=order.table) for dish in dishes_names]
  

           
            if not order_exists:
                order = Order(table=table_id, orderitems=[], waiter=waiter)
                order.orderitems = orderitems
                self.orders.append(order)
                with open(file=ORDER_PATH, mode='a', encoding='utf-8') as file:
                    headers = ['table', 'dishes', 'waiter', 'status']

                    writer = csv.DictWriter(file, fieldnames=headers)

                    writer.writerow({
                        'table': table_id,
                        'dishes': dishes_names,
                        'waiter': waiter.username,
                        'status': order.status
                    })
            else:
                existing_order.orderitems += orderitems
                existing_order.status = 'Pending'
                update_value_in_csv(
                    identifier=order.table, 
                    identifier_column='table', 
                    path=ORDER_PATH, 
                    value='Pending', 
                    value_column='status'
                )



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

            return order
        


    
    def check_orders(self):
        from auth.create_session import session
        orders = session.restourant.kitchen.current_orders

        available_orders = []

        for order in orders:
            if order.waiter == session.current_user.user.username:
                for order_item in order.orderitems:
                    if order_item.status == 'Done':
                        available_orders.append(order_item)

        for order in available_orders:
            print(order.dish, order.status)


    





         
