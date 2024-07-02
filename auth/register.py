import csv
import getpass
import re
from models.user import ROLE_CHOICES, User
from paths import USERS_PATH
from .auth import get_user, hash_password


def check_password_strength(password):
    length_regex = r'.{8,}'  # At least 8 characters long
    uppercase_regex = r'[A-Z]'  # At least one uppercase letter
    lowercase_regex = r'[a-z]'  # At least one lowercase letter
    digit_regex = r'\d'  # At least one digit
    # special_regex = r'[@$!%*?&]'  # At least one special character

    # Combine all regex patterns into a single regex using positive lookahead
    regex = (
        f'^(?=.*{length_regex})'  # At least 8 characters long
        f'(?=.*{uppercase_regex})'  # At least one uppercase letter
        f'(?=.*{lowercase_regex})'  # At least one lowercase letter
        f'(?=.*{digit_regex})'  # At least one digit
        # f'(?=.*{special_regex})'  # At least one special character
        f'.*$'
    )



    # Compile the regex pattern
    pattern = re.compile(regex)

    # Match the pattern against the password
    if re.match(pattern, password):
        return True
    else:
        return False

def check_email_valid(email):
  
    # Regex pattern for standard email format
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Check if the email matches the pattern
    if regex.match(email):
        return True
    else:
        return False


def check_role_valid(role):
    if role.title() not in ROLE_CHOICES:
        return False
    return True


def get_user_info():
    while True:
        username = input("Username: ").strip().lower()

        if not check_username_exists_valid(username):
            print('User with this username already exists.')
            break

        password = getpass.getpass("Passwrod: ").strip().lower()
        while True:
            if not check_password_strength(password):
                print('Passsword is not strong.')
                print("1. I will change the password ")
                print("2. I will Keep this password")

                option = input(">>>")

                if option == '2':
                    break
                if option == '1':
                    password = input("Passwrod: ").strip().lower()
            else:
                break
        
        email = input("Email: ").lower().strip()
        if not check_email_valid(email):
            print('Invalid Email')
            break

        role = input('Role: ')
        if not check_role_valid(role):
            print("Invalid Role")
            break
        
        password = hash_password(password)
        user = User(username=username, email=email, password=password, role=role)
        
        return user
    return None



def check_username_exists_valid(username):
    with open(file=USERS_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return False
        return True