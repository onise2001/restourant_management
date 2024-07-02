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
        # self.warehouse_worker = WarehouseWorker()
        self.distributor = Distributor
        fields = self.read_restourant()
        self.debt = float(fields['debt'])
        self.total_salary = fields['total_salary']
        self.salary_percent = fields['salary_percent']
        self.margin_percent = fields['margin_percent']
        self.commision_percent = fields['commision_percent']
        self.current_balance = fields['current_balance']


    
    def write_restourant(self):
        headers = ['debt','total_salary','salary_percent','margin_percent','commision_percent','current_balance']
        with open(RESTOURANT_PATH, mode='w') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerow({'debt':self.debt,'total_salary': self.total_salary,'salary_percent': self.salary_percent,'margin_percent': self.margin_percent,'commision_percent':self.commision_percent,'current_balance':self.current_balance})

    
    def see_warehouse_balance(self):
        balance = self.warehouse.get_balance()
        return balance
    
    def read_restourant(self):
        with open(RESTOURANT_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            fields = {}
            for line in reader:
                fields['debt'] = float(line['debt'])
                fields['total_salary'] = line['total_salary']
                fields['salary_percent'] = line['salary_percent']
                fields['margin_percent'] = line['margin_percent']
                fields['commision_percent'] = line['commision_percent']
                fields['current_balance'] = line['current_balance']
            return fields
    
    

    # @property
    # def debt(self):
    #     return self._debt
    
    # @debt.setter
    # def debt(self, amount):
    #     self._debt += amount
    #     return 
