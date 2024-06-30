from auth.auth import get_session
from paths import DISTRIBUTOR_PATH
import csv 

class Distributor:
    def __init__(self, company_name, products):
        self.company_name = company_name
        self.products = products
        self.session = get_session()


    def new_distributor(self):
        with open(DISTRIBUTOR_PATH, mode='a') as file:
            writer = csv.DictWriter(file)
            writer.writerow([{'company_name':self.company_name, 'products':self.products}])

    def get_all_distributos(self):
         with open(DISTRIBUTOR_PATH, mode='r') as file:
            reader = csv.DictReader(file)
            distributors = [Distributor(company_name=line['company_name'], products=line['products']) for line in reader]
            #writer.writerow([{'company_name':self.company_name, 'products':self.products}])
            return distributors
    
    def get_distributor(self, company_name):
        #writer.writerow([{'company_name':self.company_name, 'products':self.products}])
        distributors = self.get_all_distributos()
        for distributor in distributors:
            if company_name == distributor['company_name']:
                new_distributor = Distributor(company_name=distributor['company_name'], products=distributor['products'])
                return new_distributor
        
        return None


    def delete_distributor(self, company_name):
        distributors = self.get_all_distributos()
        
        for index,distributor in enumerate(distributors):
            if company_name == distributor['company_name']:
                distributors.pop(index) 
                self.write_all_distributors(distributors)
                return True
        
        return False
    

    def write_all_distributors(self,distributors):
        with open(DISTRIBUTOR_PATH, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['company_name', 'products'])
            writer.writeheader()
            for distr in distributors:
                writer.writerow([{'company_name': distr.company_name, 'product': distr.products}])





