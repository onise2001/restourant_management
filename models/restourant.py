from .kitchen import Kitchen
from .warehouse import Warehouse
from .worker import WarehouseWorker
from paths import RESTOURANT_PATH
import csv
from write_func import write_inital_files
class Restourant:
    def __init__(self):
        self.warehouse = Warehouse()
        self.kitchen = Kitchen()
        self.warehouse_worker = WarehouseWorker()

        with open(RESTOURANT_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.debt = line['debt']
                self.total_salary = line['total_salary']
                self.salary_percent = line['salary_percent']
                self.margin_percent = line['margin_percent']
                self.commision_percent = line['commision_percent']
                self.current_balance = line['current_balance']
    

    def write_restourant(self):
        headers = ['debt','total_salary','salary_percent','margin_percent','commision_percent','current_balance']
        write_inital_files(RESTOURANT_PATH, headers, [{'debt':self.debt,'total_salary': self.total_salary,'salary_percent': self.salary_percent,'margin_percent': self.margin_percent,'commision_percent':self.commision_percent,'current_balance':self.current_balance}])

        

