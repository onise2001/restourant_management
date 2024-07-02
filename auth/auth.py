from models.kitchen import Kitchen
from models.user import User
from models.warehouse import Warehouse
from paths import USERS_PATH
import bcrypt
import csv
from .create_session import session



def hash_password(password):
    salt = bcrypt.gensalt()
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password=password, salt=salt)
    return hashed_password.decode('utf-8')


def check_if_user_exists(username):
    with open(file=USERS_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return True
        return False


def get_user(username):
    with open(file=USERS_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return row
        return None

def authenticate_user(username, password):
    password = password.encode('utf-8')
    user = get_user(username.lower())

    if user:
        saved_password = user['password'].encode('utf-8')


        if bcrypt.checkpw(password, saved_password):
            logged_in_user = User(**user)
            print(isinstance(logged_in_user, User))
            session.current_user = logged_in_user
            session.restourant.kitchen.fill_the_kitchen()

            return logged_in_user
        else:
            print('WRONG CREDENTIALS')
            return None
    return None


def log_out_user():
    print('here')
    get_session().current_user = None
    print(get_session().current_user)


    



