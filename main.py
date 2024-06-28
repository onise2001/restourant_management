import csv, os
from models.user import User
from models.table import Table
from models.warehouse import Warehouse
from write_func import write_inital_files

def main():
    if not os.path.isdir('./restourant'):
        os.mkdir("./restourant")
        print("You are the first user, please register and set up your restourant.")
        username = input("Username: ")
        password = input("Passwrod: ")
        email = input("Email: ")
        role = "Admin"
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

            write_inital_files('./restourant/tables.csv', headers, new_tables )
        
        warehouse = Warehouse()
        headers = ['name', 'price', 'current_quantity']
        write_inital_files('./restourant/warehouse.csv', headers, warehouse.products)


        headers = ['name', 'ingredients', 'prep_method', 'price']
        write_inital_files('./restourant/dishes.csv', headers, [])

        headers = ['table', 'dishes', 'waiter', 'status']
        write_inital_files('./restourant/orders.csv', headers, [])



        








if __name__ == "__main__":
    main()