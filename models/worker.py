
from .warehouse import warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:
    def __init__(self):
        ...


    
    def check_products(self):
        for index, product in enumerate(warehouse.products):
            if product.timestamp + timedelta(days=product.days) > datetime.datetime.today():
                warehouse.products.pop(index)

        warehouse.write_products()
