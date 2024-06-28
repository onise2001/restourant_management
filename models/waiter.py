from .order import Order


class Waiter:
    def __init__(self, user):
        self.user = user
        self.orders = []
        self.permissions = {'Get Order': self.create_order, 'Add Order to Kitchen' : self.add_to_kitchen}
    

    # @user.setter
    # def user(self,user):
    #     if user.role == "Waiter":
    #         self.user = user
    #     raise ValueError("This user is not a waiter")
    
    def create_order(self, dishes):
        order = Order(orderitems=dishes, waiter=self.user)
        self.orders.append(order)
        return order
    
    def add_to_kitchen(self, order):
        from auth.auth import kitchen
        kitchen.current_orders += order

    
    def check_order_status(self, order):
        return order.status == "Finished"
    
         
