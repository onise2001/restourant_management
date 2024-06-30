import csv, os
from models.user import User
from models.table import Table
import paths
from write_func import write_inital_files
from auth.auth import hash_password, authenticate_user, get_session





def main():
    if not os.path.isdir('./restourant'):
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
        
        

    else:
        session = get_session()
        print('please login')
        username = input("Username: ")
        password = input('Password: ')


        user = authenticate_user(username, password)
        session.restourant.kitchen.fill_the_kitchen()
        

        #print(session.current_user.permissions)
        for index, (key, value) in enumerate(session.current_user.permissions.items()):
            print(f'{index + 1}. {key}')        
      

        choice = input("Choose option: ")
        session.current_user.permissions[list(session.current_user.permissions.keys())[int(choice) - 1]]()

        #print(type(session.current_user))





if __name__ == "__main__":
    main()