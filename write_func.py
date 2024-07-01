
import csv, os
from models.user import User
from models.table import Table

from auth.auth import hash_password


def create_inital_files():
        os.mkdir("./restourant")
        print("You are the first user, please register and set up your restourant.")
        username = input("Username: ").strip().lower()
        password = input("Passwrod: ").strip().lower()
        email = input("Email: ").lower().strip()
        role = "Admin"

        password = hash_password(password)
        user = User(username=username, password=password, email=email, role=role)

        

        headers = ['username', 'password', 'email', 'role']

        write_inital_files('./restourant/users.csv', headers, [{'username': user.username, 'password': user.password, 'email':user.email, 'role': user.role}]) 

        tables = input("How many tables?: ")

        if tables.isdigit():
            new_tables = []
            for i in range(1, int(tables) + 1):
                new_table = Table(number=i)
                new_tables.append({'number': new_table.number, 'status': new_table.status})

            headers = ['number', 'status']

            write_inital_files('./restourant/tables.csv', headers, new_tables)
        
        headers = ['name', 'price', 'current_quantity']
        write_inital_files('./restourant/warehouse.csv', headers, [])


        headers = ['debt', 'total_salary', 'salary_percent', 'margin_percent', 'commision_percent','current_balance']
        salary_percent = input("Salary percent: ")
        margin_percent = input("Margin percent: ")
        commision_percent = input("Commision percent: ")
        write_inital_files('./restourant/restourant.csv', headers, [{'debt': 0, 'total_salary': 0, 'salary_percent': int(salary_percent), 'margin_percent': int(margin_percent), 'commision_percent':int(commision_percent) , 'current_balance': 0}])


        headers = ['name', 'ingredients', 'prep_method', 'price']
        write_inital_files('./restourant/dishes.csv', headers, [])

        headers = ['table', 'dishes', 'waiter', 'status']
        write_inital_files('./restourant/orders.csv', headers, [])

        headers = ['id', 'order', 'dish', 'status']
        write_inital_files('./restourant/orders-items.csv', headers, [])

        headers = ['current_orders']
        write_inital_files('./restourant/kitchen.csv', headers, [])


def write_inital_files(filepath, headers, rows):
    with open(file=filepath, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)