from .warehouse import Warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:
    def __init__(self, user):
        self.user = user
        self.permissions = {'Check Products': self.check_products}

    
    def check_products(self):
        from auth.auth import session
        for index, product in enumerate(session.warehouse.products):
            if product.timestamp + timedelta(days=product.days) > datetime.datetime.today():
                session.warehouse.products.pop(index)
                print(f'{product.name} Removed')
                session.warehouse.write_products()
                
            else:

                print('all products ok')
