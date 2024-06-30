from paths import USERS_PATH
import csv
from .product import Product


# def input_password():
#     password = input("Passwrod: ").strip().lower()
#     if not check_password_strength(password):
#         print('Passsword is not strong.')
#         print("1. I will change the password ")
#         print("2. I will Keep this password")

#         option = input(">>>")

#         if option == '1':
#             input_password()
#         return password

# print(input_password())

import auth.auth
session = auth.auth.get_session()

class Admin:
    def __init__(self, user):
            
            self.user = user

            self.permissions = {'Add User': self.add_user_to_database, 'Add Products to Warehouse': self.add_product_to_warehouse, 'See current warehouse': self.see_warehouse_balance}
            


        
    def add_user_to_database(self):
        from auth.register import get_user_info

        user = get_user_info()

        if user:
            with open(file=USERS_PATH, mode='a', encoding='utf-8') as file:
                headers = ['username', 'password', 'email', 'role']

                writer = csv.DictWriter(file, fieldnames=headers)

                writer.writerow({
                    'username': user.username,
                    'password': user.password,
                    'email': user.email,
                    'role': user.role
                })
            return user
        
        return None

    def add_product_to_warehouse(self):
        name = input('Name: ')
        price = input('Price per unit: ')
        quantity = input("Quantity: ")
        days = input("Days to save: ")

        product = Product(name=name, price=price, current_quantity=quantity, days=days)

        session.restourant.warehouse.add_product(product)
        session.restourant.warehouse.write_products()
    


    def see_warehouse_balance(self):
        balance = session.restourant.warehouse.get_balance()
        return balance
         
