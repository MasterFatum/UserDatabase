from users_manage import *
from companies_manage import *


if __name__ == '__main__':
    print('Welcome to the User Management System \n')
    print('Please choose an action: \n')
    print('1. Users management \n2. Companies management \n')
    action = input('Action: ')
    match action:
        case '1':
            # clear_console()
            user_manage()
        case '2':
            # clear_console()
            company_manage()
        case _:
            print('Invalid action')




