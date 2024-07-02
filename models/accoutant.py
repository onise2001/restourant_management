from auth.create_session import get_session

class Accoutant:
    def __init__(self, user):
        self.user = user
        self.session = get_session()
        self.permissions = {'Add Distributor': self.add_distributor}


    
    def add_distributor(self,distributor):
        return self.session.distributor.new_distributor(distributor)
        


    def get_warehouse_balance(self):
        balance = self.session.restourant.warehouse.get_balance()
        return balance
    
    def get_financial_report(self):
        finances = {'debt':self.session.restourant.debt, 'salary': self.session.restourant.total_salary, 'balance': self.session.restourant.current_balance}
        return finances

    
    def pay_debt(self):
        if self.session.restourant.debt <= self.session.restourant.current_balance:
            self.session.restourant.current_balance -= self.session.restourant.debt
            self.session.restourant.debt = 0
            self.session.restourant.write_restourant()
            return True
        return False
            
    
    
    def pay_salaries(self):
        if self.session.restourant.total_salary <= self.session.restourant.current_balance:
            self.session.restourant.current_balance -= self.session.restourant.total_salary
            self.session.restourant.total_salary = 0
            self.session.restourant.write_restourant()
            return True
        return False
    
    def calculate_dish_cost(self, dish):
        price = dish.price + (dish.price * (self.session.restourant.margin_percent / 100))
        return price


    