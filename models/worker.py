from .warehouse import Warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:
    def __init__(self, user):
        self.user = user

    
    def check_products(self):
        from auth.auth import session
        for index, product in enumerate(self.warehouse.products):
            if product.timestamp + timedelta(days=product.days) > datetime.datetime.today():
                self.warehouse.products.pop(index)

        session.warehouse.write_products()
