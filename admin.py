from auth.auth import get_user, hash_password
from auth.register import check_password_strength, check_email_valid
from models.user import ROLE_CHOICES, User
from paths import USERS_PATH
import csv
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
            self.user = user


        
    def add_user_to_database(self):
        user = self.get_user_info()

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
