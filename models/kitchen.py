import ast
import csv
import os
from models.dish import Dish
from models.order_item import OrderItem
from paths import DISH_PATH, KITCHEN_PATH, ORDER_PATH
from .order import Order


class Kitchen:
    def __init__(self):
        self.current_orders = []
    

    def add_new_order_to_kitchen(self, order):
        order.status = "Preparing"
        self._current_orders.append(order)


    def display_all_order_status(self):
        for order in self.current_orders:
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
        with open(file=ORDER_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                old_order = Order(table=line['table'], orderitems=[], waiter=line['waiter'])
                for dish in ast.literal_eval(line['dishes']):
                    orderitems.append(OrderItem(dish=dish, order=old_order))
                old_order.orderitems = orderitems
                self.current_orders.append(old_order)
        
