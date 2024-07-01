import os
from write_func import create_inital_files
from auth.auth import  authenticate_user
from auth.create_session import get_session





def main():
    if not os.path.isdir('./restourant'):
        create_inital_files()
      
        
        

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