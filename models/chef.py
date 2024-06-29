import csv
from paths import ORDER_ITEM_PATH
from .dish import Dish


class Chef:

    def __init__(self, user):
        from auth.auth import kitchen

        self.user = user
        self.permissions = {
            'See orders': kitchen.display_all_order_status, 
            'Create Dish': self.create_dish, 
            'Prepare Order Item': self.prepare_order_item
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
        from auth.auth import kitchen
        kitchen.display_all_order_status()
        item_id = input('Which Order Item would you like to mark as finished? >>> ')

    
        return int(item_id)

    

    def prepare_order_item(self):
        from auth.auth import kitchen
        rows = []
        item_id = self.get_order_item()

        for order in kitchen.current_orders:
            for order_item in order.orderitems:
                if order_item.id == item_id:
                    order_item.status = 'Done'
                    with open(ORDER_ITEM_PATH, 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if int(row['id']) == int(order_item.id):
                                row['status'] = 'Done'
                            rows.append(row)

                    with open(ORDER_ITEM_PATH, 'w', newline='') as file:
                        fieldnames = rows[0].keys()
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)
                            

        return 
    

    def create_dish(self):
        from auth.auth import kitchen

        ingredients = []

        name = input('Dish Name>>> ')

        print('Please Input Ingredients>>> ')
        print('When you are done, input 1 ')

        while True: 
            ingredient = input('ingredient>>>> ')
            if ingredient.isalpha():
                ingredients.append(ingredient)
            
            elif ingredient == "1":
                break

        prep_method = input('Input prep method>>>> ')
        price = input('Price>>> ')

        new_dish = Dish(name=name, ingredients=ingredients, prep_method=prep_method, price=price)
        kitchen.save_dish(new_dish)
        return new_dish




    