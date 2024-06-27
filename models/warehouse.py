class Warehouse:
    def __init__(self, product=[]):
        self.products = product


    def add_product(self, product):
        #if product.name in [my_product.name for my_product in self.products]:
        
        for my_product in self.products:
            if my_product.name.lower() == product.name.lower():
                my_product.quantity += product.quantity
                return self.products

        self.products.append(product)
        return self.products
    
    



    
