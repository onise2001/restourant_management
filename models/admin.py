from models.user import User
from paths import USERS_PATH
import csv
from .product import Product
from utils import list_data, delete_row
import ast

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



class Admin:
    def __init__(self, user):
        from auth.create_session import get_session
        self.user = user
        self.session = get_session()
        

        self.permissions = {
            'Add User': self.add_user_to_database, 
            'Add Products to Warehouse': self.add_product_to_warehouse, 
            'See current warehouse': self.see_warehouse_balance, 
            'List Users': self.list_users,
            'Delete User': self.delete_user,
            'Edit User': self.edit_user
        }




    def list_users(self):
        # field_to_extract = ['username']
        # with open(USERS_PATH, mode='r') as file:
        #     reader = csv.DictReader(file)

        #     extracted_data = []
        #     for row in reader:
        #         extracted_row = {field: row[field] for field in field_to_extract}
        #         extracted_data.append(extracted_row)


        # print('Registered Users')
        # for data in extracted_data:
        #     for key, username in data.items():
        #         print(username)

        list_data(field='username', title='Registered Users', path=USERS_PATH)
        return
    

    def edit_user(self):
        from auth.register import check_email_valid, check_role_valid, check_username_exists_valid
        self.list_users()
        username = input('Which user would you like to edit? input username >>>> ')
        user_found = False

        with open(USERS_PATH, mode='r') as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                if row['username'] == username.lower().strip():
                    user = User(**row)
                    user_found = True
                    

        if user_found:

            headers = {
                'username': [user.username, check_username_exists_valid],
                'email': [user.email, check_email_valid],
                'role': [user.role, check_role_valid],
            }



            for field, value in headers.items():
                print(field, value[0])


            choice = input('What would you like to edit? Choose from fields:')
            

            if not choice in headers:
                print('invalid choice')
                return None
            
            edit_value = input(f'New value for {choice} field')
            field = headers[choice]

            if field[1](edit_value):

                deleted = delete_row(identifier=username, identifier_row='username', path=USERS_PATH)
                setattr(user, choice, edit_value)

                with open(USERS_PATH, 'a') as file:
                    writer = csv.DictWriter(f=file, fieldnames=['username', 'password', 'email', 'role'])
                    print(writer)
                    writer.writerow({
                        'username': user.username,
                        'email': user.email,
                        'password': user.password,
                        'role': user.role,
                    })


                print(f'{field} Changed to {edit_value}')
                return True
            else:
                print('Invalid Value')



    # def delete_user_from_database(self, username):
    #     delete_row(path=USERS_PATH, identifier_row='username', identifier=username)
    #     return

    def delete_user(self):
        self.list_users()
        username = input('Which user would you like to delete? input username >>>>')
        delete_row(identifier=username, identifier_row='username', path=USERS_PATH)
       


        
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

        self.session.restourant.warehouse.add_product(product)
        self.session.restourant.warehouse.write_products()
    


    def see_warehouse_balance(self):
        balance = self.session.restourant.see_warehouse_balance()
        [print(product) for product in balance]
        return balance
    