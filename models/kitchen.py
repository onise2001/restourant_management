import csv
import os
from paths import DISH_PATH, KITCHEN_PATH
from .order import Order


class Kitchen:

    def __init__(self):
        self.current_orders = []
        if os.path.exists(KITCHEN_PATH):
            with open(file=KITCHEN_PATH, mode='r') as file:
                
                reader = csv.DictReader(file)
                for line in reader:
                    old_order = Order(table=line['table'], dishes=line['dishes'], waiter=line['waiter'],status=line['status'])
                    self.current_orders.append(old_order)

   

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
        
