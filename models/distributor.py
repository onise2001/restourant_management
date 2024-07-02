
from paths import DISTRIBUTOR_PATH
import csv, ast 

class Distributor:
    def __init__(self, company_name=None, products=None):
        from auth.create_session import get_session
        self.company_name = company_name
        self.products = products
        self.session = get_session()

    @staticmethod
    def new_distributor(distributor):

        with open(DISTRIBUTOR_PATH, mode='a') as file:
            writer = csv.DictWriter(file,fieldnames=['company_name', 'products'])
            writer.writerow({'company_name':distributor.company_name, 'products':distributor.products})
            return True
        
    @staticmethod
    def get_all_distributos():
         with open(DISTRIBUTOR_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            distributors = [Distributor(company_name=line['company_name'], products=ast.literal_eval(line['products'])) for line in reader]
            #writer.writerow([{'company_name':self.company_name, 'products':self.products}])
            return distributors
    @staticmethod
    def get_distributor( company_name):
        #writer.writerow([{'company_name':self.company_name, 'products':self.products}])
        distributors = Distributor.get_all_distributos()
        for distributor in distributors:
            if company_name.lower() == distributor.company_name.lower():
                print(distributor.products)
               
                return distributor
        
        return None

    @staticmethod
    def delete_distributor(company_name):
        distributors = Distributor.get_all_distributos()
        
        for index,distributor in enumerate(distributors):
            if company_name == distributor['company_name']:
                distributors.pop(index) 
                Distributor.write_all_distributors(distributors)
                return True
        
        return False
    
    @staticmethod
    def write_all_distributors(self,distributors):
        with open(DISTRIBUTOR_PATH, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['company_name', 'products'])
            writer.writeheader()
            for distr in distributors:
                writer.writerow([{'company_name': distr.company_name, 'product': distr.products}])





