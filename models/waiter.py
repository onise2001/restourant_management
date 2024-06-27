from .order import Order

class Waiter:
    def __init__(self, user):
        self.user = user


    

    @user.setter
    def user(self,user):
        if user.role == "Waiter":
            self.user = user
            
        raise ValueError("This user is not a waiter")
    
    def create_order(self, dishes):
        order = Order(dishes=dishes, waiter=self.user)
        return order
    
    def check_order_status(self, order):
        return order.status == "Finished"
         
