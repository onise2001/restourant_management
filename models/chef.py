from .dish import Dish


class Chef:

    def __init__(self, user):
        from auth.auth import kitchen
        self.user == user
        self.permissions = {'See orders': kitchen.display_all_order_status, 'Create Dish': self.create_dish}
    

    @property
    def user(self):
        return self._user


    @user.setter
    def user(self, user):
        if user.role == "Chef":
            self._user == user

        raise ValueError("This user is not a chef")
    

    def prepare_order_item(self, item):
        item.status = "Finished"
        return item
    

    def create_dish(self, name):
        from auth.auth import kitchen

        ingredients = []

        name = input('Dish Name')

        print('Please Input Ingredients')
        print('When you are done, input 1')

        while True: 
            ingredient = input('ingredient')
            if ingredient.isalpha():
                ingredients.append(ingredient)
            
            elif ingredient == "1":
                break

        prep_method = input('Input prep method')
        price = input('Price')

        new_dish = Dish(name=name, ingredients=ingredients, prep_method=prep_method, price=price)
        kitchen.save_dish(new_dish)
        return new_dish




    