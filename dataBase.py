from sqlalchemy import  select,Table, Column, Integer, String, Date, MetaData, ForeignKey, create_engine
from datetime import datetime, timedelta

class DataBase:
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

    def create_database(self):
        self.database.create_all(self.engine)

    def get_user_product(self, username):
        list_to_be_returned = []
        username_to_get = (username,)
        expression = f"""SELECT products.product_name, products.expiry_date
            FROM products INNER JOIN authentification ON products.user_id == authentification.id
            WHERE authentification.username == ?;"""
        result = self.connection.execute(expression, username_to_get)
        for row in result:
            now = datetime.now()
            date_to_check = datetime.strptime(row[1], '%d-%m-%Y')
            date_to_compare = datetime.strptime(now.strftime('%d-%m-%Y'),('%d-%m-%Y'))
            if(date_to_check - timedelta(days=1) <= date_to_compare):
                list_to_be_returned += row
        return list_to_be_returned

    def login(self, username):
        username_to_get = (username,)
        expression = f"""SELECT products.product_name, products.expiry_date
            FROM products INNER JOIN authentification ON products.user_id == authentification.id
            WHERE authentification.username == ?;"""
        result = self.connection.execute(expression, username_to_get)
        return result.fetchone()

    def register(self, username, email):
        id = (self.connection.execute("SELECT MAX(id) FROM authentification;")).fetchone()[0]
        check_if_exists = (self.connection.execute("SELECT authentification.username FROM authentification WHERE authentification.username == ?;", (username, ))).fetchone()
        print((username, check_if_exists))
        if check_if_exists != username:
            data_do_get = (id + 1, username, email,)
            expression_for_insert = f"""
                INSERT INTO authentification VALUES(?,?,?)
                ;"""
            self.connection.execute(expression_for_insert, data_do_get)
        else:
            print("Username taken: Try again!")


def main():
    a = DataBase()

    a.get_user_product('spiderjako')

if __name__ == '__main__':
    main()
