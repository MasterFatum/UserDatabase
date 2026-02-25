from bll import *

def user_manage():
    while True:
        print(f'Choose you action: \n'
              f'\n1. Add user\n'
              f'2. Edit user\n'
              f'3. Remove user by ID\n'
              f'4. Remove user by E-mail\n'
              f'5. View all users\n'
              f'6. Find user by username\n'
              f'7. Authorize user\n'
              f'8. Exit \n')

        action = int(input('Action: '))

        match action:
            case 1:
                first_name = input('First name: ')
                last_name = input('Last name: ')
                email = input('E-mail: ')
                year = int(input('Year: '))
                username = input('Username: ')
                password = input('Password: ')
                get_company()
                company_name_id = int(input('Enter company ID: '))
                user = User(first_name=first_name, last_name=last_name, email=email, year_work=year, username=username, password=password, company_id=company_name_id)
                add_user(user)
            case 2:
                user_id = int(input('User ID: '))
                if user_id:
                    first_name = input('First name: ')
                    if first_name:
                        if edit_user_by_id(user_id, first_name=first_name):
                            print('User edited successfully')
                    last_name = input('Last name: ')
                    if last_name:
                        if edit_user_by_id(user_id, last_name=last_name):
                            print('User edited successfully')
                    email = input('E-mail: ')
                    if email:
                        if edit_user_by_id(user_id, email=email):
                            print('User edited successfully')
                    username = input('Username: ')
                    if username:
                        if edit_user_by_id(user_id, username=username):
                            print('User edited successfully')
                    password = input('Password: ')
                    if password:
                        if edit_user_by_id(user_id, password=password):
                            print('User edited successfully')
            case 3:
                view_all_users()
                user_id = int(input('User ID: '))
                if user_id:
                    if remove_user_by_id(user_id):
                        print('User removed successfully')
                else:
                    print('Invalid user ID')
            case 4:
                view_all_users()
                user_email = input('User E-mail: ')
                if user_email:
                    if remove_user_by_email(user_email):
                        print('User removed successfully')
            case 5:
                view_all_users()
            case 6:
                username = input('Username: ')
                if username:
                    find_user_by_username(username)
            case 7:
                username = input('Username: ')
                password = input('Password: ')
                authorize(username, password)
            case 8:
                company_name = input('Company name: ')
                if company_name:
                    add_company(company_name)
            case 9:
                get_company()
            case 10:
                exit()