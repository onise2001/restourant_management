from .order import Order
from .kitchen import kitchen

class Waiter:
    def __init__(self, user):
        self.user = user
        self.permissions = {'Get Order': self.create_order, 'Add Order to Kitchen' : self.add_to_kitchen}
    

    # @user.setter
    # def user(self,user):
    #     if user.role == "Waiter":
    #         self.user = user
            
    #     raise ValueError("This user is not a waiter")
    
    def create_order(self, dishes):
        order = Order(dishes=dishes, waiter=self.user)
        return order
    
    def add_to_kitchen(self, order):
        kitchen.current_ordes += order

    
    def check_order_status(self, order):
        return order.status == "Finished"
         
