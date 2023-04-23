from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# def session(env):
#     __engine = create_engine(f'mysql://{env.db_user}:{env.db_password}/{env.store_database}')
#     session: Session = sessionmaker(__engine)()

__engine = create_engine('mysql+mysqlconnector://mysql_user:2222@localhost/store')
session: Session = sessionmaker(__engine)()


def get_engine():
    return __engine
