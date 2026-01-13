from bll import *


if __name__ == '__main__':
    print(f'Choose you action: \n'
          f'\n1. Add user\n'
          f'2. Edit user\n'
          f'3. Remove user by ID\n'
          f'4. Remove user by E-mail\n'
          f'5. View all users\n'
          f'6. Exit\n')

action = int(input('Action: '))

match action:
    case '1':
        pass
    case '2':
        pass
    case '3':
        pass
    case '4':
        pass
    case '5':
        pass
    case '6':
        exit()