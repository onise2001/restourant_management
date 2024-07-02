from .warehouse import Warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:

    def __init__(self,user):
        from auth.create_session import get_session
        self.user = user
        self.session = get_session()
        self.permissions = {'Drop expired products': self.check_products}


    
    def check_products(self):

        for index, product in enumerate(self.session.restourant.warehouse.products):
            if product.timestamp + timedelta(days=int(product.days)) <= datetime.datetime.today().date() or product.current_quantity == '0':
                self.session.restourant.warehouse.products.pop(index)

        self.session.restourant.warehouse.write_products()

