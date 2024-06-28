import csv, os
from models.user import User
from models.table import Table
from write_func import write_inital_files
from auth.auth import hash_password, authenticate_user, session

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

            write_inital_files('./restourant/tables.csv', headers, new_tables )

    else:

        print('please login')
        username = input("Username: ")
        password = input('Password: ')


        user = authenticate_user(username, password)
        print(session.current_user.user.username)
     
        print(type(session.current_user))


        session.current_user.add_user_to_database()

        print(session.current_user.permissions)



if __name__ == "__main__":
    main()