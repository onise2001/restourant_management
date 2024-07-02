from .product import Product
from .distributor import Distributor
from paths import PAYMENTS_PATH
import csv
class Accoutant:

    def __init__(self, user):
        from auth.create_session import get_session

        self.user = user
        self.session = get_session()
        self.permissions = {'Proccess pending payments': self.get_payment,'Add Distributor': self.add_distributor, 'Delete Distributor': self.delete_distributor,'See Financial Report': self.get_financial_report, 'Get products from distributor': self.get_products_from_distributor, "Pay salaries": self.pay_salaries, 'Pay debt':self.pay_debt}


    
    def add_distributor(self):
        company_name = input("Company Name: ")
        products = []

        while True:
            name = input('Name: ')
            price = input('Price per unit: ')

            if name == '1' or price == '1':
                break
            
            product = {'name': name, 'price': price}
            products.append(product)

        distributor = Distributor(company_name=company_name, products=products)
        
        return self.session.restourant.distributor.new_distributor(distributor)
        
    def delete_distributor(self):
        name = input('Company Name: ')
        if self.session.restourant.distributor.delete_distributor(name):
            print('Distributor Deleted')
        else:
            print('No such distributor')


    def get_warehouse_balance(self):
        balance = self.session.restourant.warehouse.get_balance()
        return balance
    
    def get_financial_report(self):
        finances = {'debt':self.session.restourant.debt, 'salary': self.session.restourant.total_salary, 'balance': self.session.restourant.current_balance}
        print(f'Balance: {finances["balance"]}\nSalary to pay: {finances['salary']}\nDebt: {finances["debt"]}')
        return finances

    
    def pay_debt(self):
        if self.session.restourant.debt <= self.session.restourant.current_balance:
            self.session.restourant.current_balance -= self.session.restourant.debt
            self.session.restourant.debt = 0
            self.session.restourant.write_restourant()
            print("Debt Paid.")
            
        print("Not enough balance to pay Debt")
            
    
    
    def pay_salaries(self):
        self.session.restourant.total_salary = 0
        self.session.restourant.write_restourant()
        print("Salaries Paid.")
            
       
    def get_payment(self):
        pending_payments = self.read_pending_payments()

        for amount in pending_payments:
            if not isinstance(amount, (int, float)):
                print(f"Invalid amount type: {type(amount)} with value {amount}")
                continue  # Skip this amount and continue with the next one
    
            salary = (amount / 100) * self.session.restourant.salary_percent
            commision = (amount / 100) * self.session.restourant.commision_percent
            amount -= salary + commision
            self.session.restourant.current_balance += amount
            self.session.restourant.total_salary += salary + commision
        
        self.session.restourant.write_restourant()


    def read_pending_payments(self):
        payments = []

        with open(PAYMENTS_PATH, mode='r') as file:
            reader = csv.DictReader(file)

            for line in reader:
                print(type(float(line['amount'])))
                payments.append(float(line['amount']))

            return payments





    
    def calculate_dish_cost(self, dish):
        price = dish.price + (dish.price * (self.session.restourant.margin_percent / 100))

        return price
    

    def get_products_from_distributor(self):
        company_name = input('Company name: ')
        distributor = self.session.restourant.distributor.get_distributor(company_name)
        total = 0
        if distributor is not None:

            for product in list(distributor.products):
                print(f'Name: {product['name']}\nPrice per unit: {product['price']}')
                amount = input("Amount: ")
                total += float(amount) * float(product['price'])
                days = input("Days to expiration: ")
                new_product = Product(name=product['name'], price=product['price'], current_quantity=amount, days=days)
                self.session.restourant.warehouse.add_product(new_product)
            
            self.session.restourant.debt += total
            self.session.restourant.write_restourant()

            return 
        
        print('No such distributor, would you like to add one?')
        while True:
            choice = input('1.Yes\n2.No')
            if choice == '1':
                self.add_distributor()
                break
            elif choice == '2':
                break




    