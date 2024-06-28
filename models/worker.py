
from .warehouse import Warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:
    def __init__(self):
        self.warehouse = Warehouse()


    
    def check_products(self):
        for index, product in enumerate(self.warehouse.products):
            if product.timestamp + timedelta(days=product.days) > datetime.datetime.today():
                self.warehouse.products.pop(index)

        self.warehouse.write_products()
