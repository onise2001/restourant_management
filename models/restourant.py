from .kitchen import Kitchen
from .warehouse import Warehouse
from .worker import WarehouseWorker
from .distributor import Distributor
from paths import RESTOURANT_PATH
import csv
#from write_func import write_inital_files
class Restourant:
    def __init__(self):
        self.warehouse = Warehouse()
        self.kitchen = Kitchen()
        self.warehouse_worker = WarehouseWorker()
        self.distributor = Distributor

        with open(RESTOURANT_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.debt = line['debt']
                self.total_salary = line['total_salary']
                self.salary_percent = line['salary_percent']
                self.margin_percent = line['margin_percent']
                self.commision_percent = line['commision_percent']
                self.current_balance = line['current_balance']
    

    # def write_restourant(self):
    #     headers = ['debt','total_salary','salary_percent','margin_percent','commision_percent','current_balance']
    #     with open(RESTOURANT_PATH, m=wr)
    #     write_inital_files(RESTOURANT_PATH, headers, [{'debt':self.debt,'total_salary': self.total_salary,'salary_percent': self.salary_percent,'margin_percent': self.margin_percent,'commision_percent':self.commision_percent,'current_balance':self.current_balance}])

    
    def see_warehouse_balance(self):
        balance = self.warehouse.get_balance()
        return balance

