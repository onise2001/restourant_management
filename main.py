
import os
from write_func import create_inital_files
from auth.auth import  authenticate_user, log_out_user
from auth.create_session import get_session







def main():
    while True:
        if not os.path.isdir('./restourant'):
            create_inital_files()

            
        else:
            session = get_session()
            
            if not session.current_user:
                print('please login')
                username = input("Username: ")
                password = input('Password: ')

            
                user = authenticate_user(username, password)

            if user:
                # logout = {'Log Out': log_out_user}
                # session.current_user.permissions.update(logout)
                # session.restourant.kitchen.fill_the_kitchen()
                logout = {'Log Out': log_out_user}
                session.current_user.permissions.update(logout)
                
                # print(session.current_user.permissions)
                print('*' * 20)
                print('0. Exit')
                
                

                for index, (key, value) in enumerate(session.current_user.permissions.items()):
                    print(f'{index + 1}. {key}')        
            

                choice = input("Choose option: ")


                if choice == '0':
                    break


                try:
                    session.current_user.permissions[list(session.current_user.permissions.keys())[int(choice) - 1]]()
                except ValueError:
                    continue

            else: 
                continue





if __name__ == "__main__":
    main()