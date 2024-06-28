from dish import Dish
class Chef:

    def __init__(self, user):
        self.user == user
    

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
    

    def create_dish(self,name, ingredients,  prep_method, price):
        new_dish = Dish(name=name,ingredients=ingredients, prep_method=prep_method, price=price)
        return new_dish




    