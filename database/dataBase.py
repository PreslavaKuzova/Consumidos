from sqlalchemy import  select,Table, Column, Integer, String, Date, MetaData, ForeignKey, create_engine
from datetime import datetime, timedelta


def create_table():
    engine = create_engine('sqlite:///test.db', echo = False)
    connection = engine.connect()
    database = MetaData()
    if not engine.dialect.has_table(engine, 'authentification') or not engine.dialect.has_table(engine, 'products'): 
        authentification = Table('authentification', database,
            Column('id', Integer, primary_key = True),
            Column('username', String),
            Column('email', String))

        products = Table('products', database,
            Column('id', Integer, primary_key = True),
            Column('user_id', None, ForeignKey('authentification.id')),
            Column('product_name', String),
            Column('expiry_date', Date))

if __name__ == '__main__':
    main()
