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
            'Delete User': self.delete_user
        }




    def list_users(self):
        field_to_extract = ['username']
        with open(USERS_PATH, mode='r') as file:
            reader = csv.DictReader(file)

            extracted_data = []
            for row in reader:
                extracted_row = {field: row[field] for field in field_to_extract}
                extracted_data.append(extracted_row)


        print('Registered Users')
        for data in extracted_data:
            for key, username in data.items():
                print(username)

        return
    
    
    def delete_user(self):

        self.list_users()
        username = input('Which user would you like to delete? input username >>>>')

        rows = []
        user_deleted = False
        with open(USERS_PATH, mode='r') as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                if not row['username'] == username.lower().strip():
                    rows.append(row)
                else:
                    user_deleted = True



        with open(USERS_PATH, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        if user_deleted:
            print(f'User {username} deleted')
            return True
       
        print(f'User {username} not found')
        return False




        
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
    