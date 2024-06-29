import datetime
class Product:
    
    def __init__(self, name, price,current_quantity,days,timestamp=datetime.datetime.date(datetime.datetime.today())):
        self.name = name
        self.price = price
        self.current_quantity = current_quantity
        self.timestamp = timestamp
        self.days = days
        

    

