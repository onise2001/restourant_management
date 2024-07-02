import ast
import csv
import os
from models.dish import Dish
from models.order_item import OrderItem
from paths import DISH_PATH, KITCHEN_PATH, ORDER_ITEM_PATH, ORDER_PATH, WAREHOUSE_PATH
from .order import Order


class Kitchen:
    def __init__(self):
        self.current_orders = []
    

    def add_new_order_to_kitchen(self, order):
        order.status = "Preparing"
        self._current_orders.append(order)


    def display_all_order_status(self):
        for order in self.current_orders:
            if order.status != 'Finished':
                order.order_status()


    def save_dish(self, dish):
        with open(file=DISH_PATH, mode='a', encoding='utf-8') as file:
            headers = ['name', 'ingredients', 'prep_method', 'price']


            writer = csv.DictWriter(file, fieldnames=headers)

        
            writer.writerow({
                'name': dish.name,
                'ingredients': dish.ingredients,
                'prep_method': dish.prep_method,
                'price': dish.price
            })

        return dish
    
    def fill_the_kitchen(self):
        orderitems = []
        orderitem_dict = {}
        self.current_orders = []
        with open(file=ORDER_ITEM_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                orderitem = OrderItem(id=line['id'], order_table=line['order_table'], dish=line['dish'], status=line['status'])

                # if orderitem.order_table not in orderitem_dict:
                #     orderitem_dict[orderitem.order_table] = [orderitem]
                # else:
                #     orderitem_dict[orderitem.order_table].append(orderitem)

                orderitems.append(orderitem)
                


        with open(file=ORDER_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                old_order = Order(table=line['table'], orderitems=[], waiter=line['waiter'], status=line['status'], payement=line['payment'])
                
                orderitem_ids = [int(orderitem.id) for orderitem in orderitems]
                saved_orderitems_ids = ast.literal_eval(line['orderitem_ids'])

                common_ids = list(set(orderitem_ids) & set(saved_orderitems_ids))

                # orderitems = orderitem_dict[f'{old_order.table}']
                # old_order.orderitems = orderitems
                if old_order.payement == 'Unpaid':
                    for orderitem in orderitems:
                        if int(orderitem.id) in common_ids:
                            old_order.orderitems.append(orderitem)

                    self.current_orders.append(old_order)
            return
        
    def check_ingredient_in_database(self, ingredient):
        with open(WAREHOUSE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == ingredient:
                    return True
            
        return False
    

    def check_if_enough_ingredients(self, dish):
        from auth.create_session import session
        ingredients = None
        with open(DISH_PATH, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['name'] == dish:
                    ingredients = ast.literal_eval(row['ingredients'])
            
        doable_counter = 0
        if ingredients:
            for ingredient in ingredients:
                for ingredient_name, ingredient_value in ingredient.items():
                    if self.extract_ingredients(ingredient_name, ingredient_value):
                        doable_counter += 1
                    else:
                        print(ingredient_name, 'Not Enough')

        if len(ingredients) == doable_counter:
            return True
        return False
    
    # Extract ingredients from database if there are enough.

    # If prevoiusly added product amount is not enough, it will be 
    # accumulated with later added product amounts.
    
    def extract_ingredients(self, ingredient, quantity):
        all_saved_ingredient = []

        from auth.create_session import session
        for product in session.restourant.warehouse.products:
            if product.name == ingredient:
                all_saved_ingredient.append(product)

        sorted_products = sorted(all_saved_ingredient, key=lambda product: product.timestamp)
        ingredient_quantity_sum = 0

        for product in sorted_products:
            ingredient_quantity_sum += float(product.current_quantity)

            if ingredient_quantity_sum - float(quantity) >= 0:
                product.current_quantity = ingredient_quantity_sum - float(quantity)
                return True
            else:
                product.current_quantity = 0
        
        return False
    
   
        


