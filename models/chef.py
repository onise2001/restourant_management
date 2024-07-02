import ast
import csv
from paths import DISH_PATH, ORDER_ITEM_PATH
from .dish import Dish
from update_func import update_value_in_csv
from utils import list_data, delete_row

class Chef:

    def __init__(self, user):
        from auth.auth import log_out_user

        from auth.create_session import session

        self.user = user
        self.permissions = {
            'See orders': session.restourant.kitchen.display_all_order_status, 

            'Create Dish': self.create_dish, 
            'Prepare Order Item': self.prepare_order_item,
            'Delete Dish': self.delete_dish,
            'List Dishes': self.list_dishes,
            'Update Dish': self.update_dish
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

        from auth.create_session import session
        session.restourant.kitchen.display_all_order_status()

        item_id = input('Which Order Item would you like to mark as finished? >>> ')

        return int(item_id)

    

    def prepare_order_item(self):

       
        item_id = self.get_order_item()

        for order in session.restourant.kitchen.current_orders:

            for order_item in order.orderitems:
                if int(order_item.id) == item_id:
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

        from auth.create_session import session



        name = input('Dish Name>>> ')

        print('Please Input Ingredients>>> ')
        print('When you are done, please input 1 ')
        

 
        ingredients = self.gather_ingredient_info()


        prep_method = input('Input prep method>>>> ')
        price = input('Price>>> ')

        new_dish = Dish(name=name.lower(), ingredients=ingredients, prep_method=prep_method, price=price)
        session.restourant.kitchen.save_dish(new_dish)
        return new_dish


    def list_dishes(self):
        list_data(field='name', title='Registered Dishes', path=DISH_PATH)

        return


    def delete_dish(self):
        self.list_dishes()
        dish = input('Input dish that you would like to delete')
        delete_row(identifier=dish, identifier_row='name', path=DISH_PATH)
        return
    

    def update_dish(self):
        self.list_dishes()

        dish = input('Which dish would you like update?')

        dish_found = False
        with open(DISH_PATH, mode='r') as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                if row['name'] == dish.lower().strip():
                    row['ingredients'] = ast.literal_eval(row['ingredients'])

                    dish = Dish(**row)
                    dish_found = True
                    

        if dish_found:

            headers = {
                'ingredients': dish.ingredients,
                'name': dish.name,
                'prep_method': dish.prep_method,
                'price': dish.price 
            }


            for field, value in headers.items():
                print(field, value)


            choice = input('What would you like to edit? Choose from fields:')
            

            if not choice in headers:
                print('invalid choice')
                return None
            

            if choice == 'ingredients':
                print('1. Add')
                print('2. Remove')
                ingredient_choice = input('Would you like to add or remove ingredients?')

                if ingredient_choice == '1':

                    print('Input ingredients that you would like to add')
                    print('Input 1 to terminate the process')
                    edit_values = self.gather_ingredient_info()
                    edit_value = dish.ingredients + edit_values

                elif ingredient_choice == '2':
                    [print(ingredient) for ingredient in dish.ingredients]
                    ingredient_input = input('Which ingredient would you like to remove?')
                    
                    for ingredient_data in dish.ingredients:

                        if ingredient_input in ingredient_data:
                            dish.ingredients.remove(ingredient_data)
                            break
                    
                        
                    edit_value = dish.ingredients

                    

            else:   
                edit_value = input(f'New value for {choice} field')


            field = headers[choice]


            deleted = delete_row(identifier=dish.name, identifier_row='name', path=DISH_PATH)
            setattr(dish, choice, edit_value)

            with open(DISH_PATH, 'a') as file:
                writer = csv.DictWriter(f=file, fieldnames=['name', 'ingredients', 'prep_method', 'price'])
                print(writer)
                writer.writerow({
                    'name': dish.name,
                    'ingredients': dish.ingredients,
                    'prep_method': dish.prep_method,
                    'price': dish.price,
                })


            print(f'{field} Changed to {edit_value}')
            return True


    def gather_ingredient_info(self):
        from auth.create_session import session
        ingredients = []

        while True: 
            ingredient = input('ingredient>>> ')

            if ingredient.isalpha() and self.session.restourant.warehouse.check_ingredient_in_database(ingredient=ingredient) != None:

                amount = input('amount>>>')
                ingredient_data = {f'{ingredient}': amount}
                ingredients.append(ingredient_data)
                price += self.session.restourant.warehouse.check_ingredient_in_database(ingredient=ingredient)
            
            elif ingredient == "1":
                break

            else:
                answer = input('Would you like to add ingredient to the database? y/n>>> ')

                if answer.lower().strip() == 'y' or 'yes':
                    self.session.restourant.warehouse.add_ingredient_to_warehouse()

                
                else:
                    continue



        return ingredients
