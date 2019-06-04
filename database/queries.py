import sys
import os
from sqlalchemy import  select,Table, Column, Integer, String, Date, MetaData, ForeignKey, create_engine
from datetime import datetime, timedelta
from dataBase import create_table
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{path}')

os.chdir(f'{path}')
engine = create_engine('sqlite:///test.db', echo = False)
connection = engine.connect()
database = MetaData()

authentification = Table('authentification', database,
    Column('id', Integer, primary_key = True),
    Column('username', String),
    Column('email', String))

products = Table('products', database,
    Column('id', Integer, primary_key = True),
    Column('user_id', None, ForeignKey('authentification.id')),
    Column('product_name', String),
    Column('expiry_date', Date))


def create_database():
    database.create_all(engine)


def get_all_user_products(username):
    username_to_get = (username,)
    expression = f"""SELECT products.product_name, products.expiry_date
        FROM products INNER JOIN authentification ON products.user_id == authentification.id
        WHERE authentification.username == ?;"""
    result = connection.execute(expression, username_to_get)
    return result.fetchall()

def add_new_user(username, email):
    id = (connection.execute("SELECT MAX(id) FROM authentification;")).fetchone()[0]
    check_if_exists = (connection.execute("SELECT authentification.username FROM authentification WHERE authentification.username == ?;", (username, ))).fetchone()
    if check_if_exists != username:
        data_do_get = (id + 1, username, email,)
        expression_for_insert = f"""
            INSERT INTO authentification VALUES(?,?,?)
            ;"""
        connection.execute(expression_for_insert, data_do_get)
        print("User registered!")
    else:
        print("Username taken: Try again!")

def get_current_user_email(username):
    username_to_get = (username,)
    expression = f"""SELECT email
        FROM authentification
        WHERE username == ?;"""
    result = connection.execute(expression, username_to_get)
    to_be_returned =result.fetchone()[0] 
    return to_be_returned

def sign_in_user(username):
    username_to_get = (username,)
    expression = f"""SELECT id
        FROM authentification
        WHERE username == ?;"""
    result = connection.execute(expression, username_to_get)
    to_be_returned = result.fetchone()
    if not (to_be_returned is None): 
        return to_be_returned

def delete_user(username):
    user_to_delete = (username,)
    id = connection.execute("SELECT id FROM authentification WHERE username == ?", user_to_delete).fetchone()[0]
    products_to_delete = (id,)
    expression = f"""DELETE FROM authentification
        WHERE authentification.username == ?;"""
    connection.execute(expression, user_to_delete)
    expression = f"""DELETE FROM products
        WHERE products.user_id == ?;"""
    connection.execute(expression, products_to_delete)

def get_all_user_products_that_expire(username):
    list_to_be_returned = []
    username_to_get = (username,)
    expression = f"""SELECT products.product_name, products.expiry_date
        FROM products INNER JOIN authentification ON products.user_id == authentification.id
        WHERE authentification.username == ?;"""
    result = connection.execute(expression, username_to_get)
    for row in result:
        now = datetime.now()
        date_to_check = datetime.strptime(row[1], '%d-%m-%Y')
        date_to_compare = datetime.strptime(now.strftime('%d-%m-%Y'),('%d-%m-%Y'))
        if(date_to_check - timedelta(days=1) <= date_to_compare):
            list_to_be_returned.append(tuple(row))
    return list_to_be_returned

def get_products_by_id(id):
    id_to_get = (id,)
    expression = f"""SELECT product_name
        FROM products
        WHERE id == ?;"""
    return connection.execute(expression, id_to_get).fetchone()[0]

def get_products_by_expiry_date(expiry_date):
    expiry_to_get = (expiry_date,)
    expression = f"""SELECT product_name
        FROM products
        WHERE expiry_date == ?;"""
    return connection.execute(expression, expiry_to_get).fetchall()


def add_food(current_user, food_name, expiry):
    current_user_food = (current_user,)
    id = (connection.execute("SELECT MAX(id) FROM products;")).fetchone()[0]
    user_id = connection.execute("SELECT id FROM authentification WHERE username == ?", current_user_food).fetchone()[0]
    products_to_add = (id, user_id, food_name, expiry)
    expression = f"""INSERT INTO products
        VALUES(?,?,?,?);"""
    connection.execute(expression, products_to_add)

def delete_food(current_user, food_name):
    current_user_food = (current_user,)
    id = connection.execute("SELECT id FROM authentification WHERE username == ?", current_user_food).fetchone()[0]
    products_to_delete = (food_name, id)
    expression = f"""DELETE FROM products
        WHERE products.product_name == ? AND products.user_id == ?;"""
    connection.execute(expression, products_to_delete)


if __name__ == '__main__':
    main()