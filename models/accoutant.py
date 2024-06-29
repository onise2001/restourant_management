class Accoutant:

    def __init__(self, user):
        self.user = user


    
    def get_warehouse_balance(self):
        ...
    
    def calculate_dish_cost(self, dish):
        price = 0
        for ingredient in dish.ingredients:
            price += float(ingredient.price)

        return price


    