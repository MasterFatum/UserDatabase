from sqlalchemy import create_engine, select, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship

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

def get_company():
    for company in db.query(Company).all():
        print(
            f'Id: {company.id}\n'
            f'Company name: {company.name}\n'
            + f'{"=" * 30}')

def add_company(company):
    try:
        company_name = Company(name=company)
        db.add(company_name)
        print(f'Added company: {company}')
    except Exception as e:
        print(e)

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
    for user in db.query(User).all():
        print(
              f'Id: {user.id}\n'
              f'First name: {user.first_name}\nL'
              f'Last name: {user.last_name}\n'
              f'Username: {user.username}\n'
              f'Email: {user.email}\n'
              f'Password: {user.password}\n'
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
