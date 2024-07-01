import csv
from paths import ORDER_ITEM_PATH
from .dish import Dish
from update_func import update_value_in_csv


class Chef:

    def __init__(self, user):
        from auth.auth import session, log_out_user

        self.user = user
        self.permissions = {
            'See orders': session.kitchen.display_all_order_status, 
            'Create Dish': self.create_dish, 
            'Prepare Order Item': self.prepare_order_item,
        }
    

    @property
    def user(self):
        return self._user


    @user.setter
    def user(self, user):
        print(user.role)
        if user.role == "Chef":
            self._user = user
            return
        
        raise ValueError("This user is not a chef")
    
    def get_order_item(self):
        from auth.auth import session
        session.kitchen.display_all_order_status()
        item_id = input('Which Order Item would you like to mark as finished? >>> ')

    
        return int(item_id)

    

    def prepare_order_item(self):
        from auth.auth import session
        rows = []
        item_id = self.get_order_item()

        for order in session.kitchen.current_orders:
            for order_item in order.orderitems:
                if order_item.id == item_id:
                    order_item.status = 'Done'
                

                    update_value_in_csv(
                        identifier=str(order_item.id), 
                        identifier_column='id', 
                        value='Done', 
                        value_column='status', 
                        path=ORDER_ITEM_PATH
                    )


                            

        return 
    

    def create_dish(self):
        # TODO if no product, ask chef to create it and also specify the price
        from auth.auth import session

        ingredients = []

        name = input('Dish Name>>> ')

        print('Please Input Ingredients>>> ')
        print('When you are done, please input 1 ')
        

        while True: 
            ingredient = input('ingredient>>> ')
            if ingredient.isalpha() and session.kitchen.check_ingredient_in_database(ingredient=ingredient):
                amount = input('amount>>>')
                ingredient_data = {f'{ingredient}': amount}
                ingredients.append(ingredient_data)
            
            elif ingredient == "1":
                break

            else:
                answer = input('Would you like to add ingredient to the database? y/n>>> ')

                if answer.lower().strip() == 'y' or 'yes':
                    session.warehouse.add_ingredient_to_warehouse()
                
                else:
                    continue



        prep_method = input('Input prep method>>>> ')
        price = input('Price>>> ')

        new_dish = Dish(name=name, ingredients=ingredients, prep_method=prep_method, price=price)
        session.kitchen.save_dish(new_dish)
        return new_dish




    