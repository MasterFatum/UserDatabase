from bll import *


def company_manage():
    while True:
        print(f'Choose you action: \n'
              f'\n1. Add company\n'
              f'2. Remove company\n'
              f'3. View company\n'
              )

        action = int(input('Action: '))
        match action:
            case 1:
                company_name = input('Company name: ')
                add_company(company_name)
            case 2:
                remove_company()
            case 3:
                get_company()