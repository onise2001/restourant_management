import csv
from .order import Order
class Kitchen:

    def __new__(self):
        self.current_orders = []
        with open(file = '../restourant/kitchen.csv', mode='r') as file:
            
            reader = csv.DictReader(file)
            for line in reader:
                old_order = Order(table=line['table'],dishes=line['dishes'], waiter=line['waiter'],status=line['status'])
                self.current_orders.append(old_order)
    


    @property
    def current_orders(self):
        return self._current_orders
    
    @current_orders.setter
    def current_orders(self, order):
        self._current_orders.append(order)






