
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
               
                logout = {'Log Out': log_out_user}
                session.current_user.permissions.update(logout)
                
                print('*' * 20)
                print('0. Exit')
                
                if user.role == "Admin":
                   admin_menu_management(session.current_user.permissions)

                else:
                    key = menu_management(session.current_user.permissions)
                    session.current_user.permissions[key]()


            else: 
                continue


def admin_menu_management(permissions):

    outer_key = menu_management(permissions)
    if outer_key == "Log Out":
        permissions[outer_key]()
        return
    
    inner_key = menu_management(permissions[outer_key])

    permissions[outer_key][inner_key]()




def menu_management(menu):
    for index, (key, value) in enumerate(menu.items()):
        print(f'{index + 1}. {key}')        

    choice = input("Choose option: ")
    if choice == '0':
        return
        
    key = list(menu.keys())[int(choice) - 1]
    
    return key



if __name__ == "__main__":
    main()