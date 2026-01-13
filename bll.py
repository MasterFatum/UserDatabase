from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///users.db', echo=True)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)

with Session() as session:
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Base.metadata.create_all(engine)

# root = User(first_name='Panfilov', last_name='Ivan', username='root', email='root@root.ru', password='Doberman777')
# session.add(root)
# session.commit()


def add_user(user):
    user = User()
    session.add(user)
    session.commit()
    print(f'Added user: {user.email}')


def remove_user_by_id(id):
    user = session.query(User).get(id)
    if user:
        session.delete(user)
        session.commit()
        print(f'Removed user: {user.email}')


def remove_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    if user:
        session.delete(user)
        session.commit()
        print(f'Removed user: {email}')


def view_all_users():
    for user in session.query(User).all():
        print(f'First name: {user.first_name}\nL'
              f'ast name: {user.last_name}\n'
              f'Username: {user.username}\n'
              f'Email: {user.email}\n'
              f'Password: {user.password}\n'
              + f'{"=" * 30}')