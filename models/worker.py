from .warehouse import Warehouse
from datetime import timedelta 
import datetime
class WarehouseWorker:
    def __init__(self):
        ...
        #from auth.create_session import get_session
        #self.user = user
        #self.session = get_session()


    
    # def check_products(self):

    #     for index, product in enumerate(self.session.restourant.warehouse.products):
    #         if product.timestamp + timedelta(days=product.days) > datetime.datetime.today() or product.current_quantity == 0:
    #             self.session.warehouse.products.pop(index)

    #     self.session.warehouse.write_products()
