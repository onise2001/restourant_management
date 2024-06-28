import csv
from paths import KITCHEN_PATH
from .product import Product

class Warehouse:
    def __init__(self):
        self.products = []
        with open(file=KITCHEN_PATH, mode='r') as file:
            
            reader = csv.DictReader(file)
            for line in reader:
                old_order = Product(name=line['name'],price=line['price'], current_quantity=line['current_quantity'],timestamp=line['timestamp'], days=line['days'])
                self.products.append(old_order)



    def add_product(self, product):
        #if product.name in [my_product.name for my_product in self.products]:
        
        for my_product in self.products:
            if my_product.name.lower() == product.name.lower():
                my_product.quantity += product.quantity
                return self.products

        self.products.append(product)
        return self.products
    



    
    def write_products(self):
        with open('restourant/warehouse.csv', mode='w') as file:
            writer = csv.DictWriter(f=file,fieldnames=['name', 'price', 'current_quantity', 'timestamp', 'days'])
            writer.writeheader()
            writer.writerows([{'name': product.name, 'price':product.price, 'current_quantity': product.current_quantity, 'timestamp': product.timestamp, 'days': product.days} for product in self.products])
    
    


    
