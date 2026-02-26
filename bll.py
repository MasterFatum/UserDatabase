from sqlalchemy import create_engine, select, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
import os

engine = create_engine('sqlite:///users.db')

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)

with Session() as db:
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    year_work = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="users")


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="company")

# Base.metadata.create_all(engine)


# tom = User(first_name='Tom', last_name='Smith', username='tom', email='tom@tom.com', password='123456', year_work=2026, company_id=1)
# db.add(tom)
# db.commit()

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')
# clear_console()

def get_companies():
    companies = db.query(Company).all()
    if companies:
        for company in companies:
            print(
            f'Id: {company.id}\n'
            f'Company name: {company.name}\n'
            + f'{"=" * 30}')
    else:
        print('No companies')


def add_company(company):
    try:
        company_name = Company(name=company)
        db.add(company_name)
        db.commit()
        print(f'Added company: {company}')
    except Exception as e:
        print(e)


def remove_company(id):
    company = db.query(Company).get(id)
    if company:
        db.delete(company)
        db.commit()
        print(f'Removed company: {company.name}')



def add_user(user):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f'Added user: {user.email}')
    except Exception as e:
        print(e)


def edit_user_by_id(id, **kwargs):
    if kwargs:
        user = db.query(User).get(id)
        if user:
            if kwargs.get('first_name'):
                user.first_name = kwargs.get('first_name', user.first_name)
            if kwargs.get('last_name'):
                user.last_name = kwargs.get('last_name', user.last_name)
            if kwargs.get('username'):
                user.username = kwargs.get('username', user.username)
            if kwargs.get('password'):
                user.password = kwargs.get('password', user.password)
            if kwargs.get('email'):
                if not get_all_usernames(kwargs.get('email')):
                    user.email = kwargs.get('email', user.email)
                else:
                    print('This email is already taken')
            db.commit()
            print(f'Updated user: {user.email}')


def remove_user_by_id(id):
    user = db.query(User).get(id)
    if user:
        db.delete(user)
        db.commit()
        print(f'Removed user: {user.email}')


def remove_user_by_email(email):
    user = db.query(User).filter_by(email=email).first()
    if user:
        db.delete(user)
        db.commit()
        print(f'Removed user: {email}')


def view_all_users():
    users = db.query(User).all()
    for user in users:
        print(
              f'Id: {user.id}\n'
              f'First name: {user.first_name}\nL'
              f'Last name: {user.last_name}\n'
              f'Username: {user.username}\n'
              f'Email: {user.email}\n'
              f'Password: {user.password}\n'
              f'Company: {user.company.name}\n'
              f'Year work: {user.year_work}\n'
              + f'{"=" * 30}')


def find_user_by_username(username):
    user = db.query(User).filter_by(username=username).first()
    if user:
        print(
            f'Id: {user.id}\n'
            f'First name: {user.first_name}\nL'
            f'Last name: {user.last_name}\n'
            f'Username: {user.username}\n'
            f'Email: {user.email}\n'
            f'Password: {user.password}\n'
            + f'{"=" * 30}')


def get_all_usernames(username):
    usernames = db.query(User).filter_by(username=username).first()
    if usernames:
        return True
    return False


def authorize(username, password):
    user = db.query(User).filter_by(username=username).first()
    if user:
        if user.password == password:
            print(f'Welcome, {user.first_name} {user.last_name}!')
            return True
        else:
            print('Incorrect password.')
            return False
    else:
        print('User not found.')
        return False


# ... существующий код ...

def get_users_by_company(company_id):
    """
    Выводит всех пользователей, которые работают в компании с указанным company_id.
    """
    company = db.query(Company).get(company_id)
    if company:
        users = db.query(User).filter_by(company_id=company.id).all()
        if users:
            print(f"Users working in '{company.name}':")
            for user in users:
                print(
                    f'Id: {user.id}\n'
                    f'Company: {company.name}\n'
                    f'First name: {user.first_name}\n'
                    f'Last name: {user.last_name}\n'
                    f'Username: {user.username}\n'
                    f'Email: {user.email}\n'
                    f'Year work: {user.year_work}\n'
                    + f'{"=" * 30}')
        else:
            print(f'No users found in company: {company.name}')
    else:
        print('Company not found.')

# ... остальной код ...