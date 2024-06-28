import datetime
class Product:
    
    def __init__(self, name, price,current_quantity,days):
        self.name = name
        self.price = price
        self.current_quantity = current_quantity
        self.timestamp = datetime.datetime.today()
        self.days = days

    

