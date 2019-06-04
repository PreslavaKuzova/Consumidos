import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{path}/../database')

import dataBase
import queries


class MainController:
    @classmethod
    def get_user_email(cls, username):
        return queries.get_current_user_email(username)

    @classmethod
    def get_user_to_soon_expire_products(cls, username):
        return queries.get_all_user_products_that_expire(username)

    @classmethod
    def insert_food(cls, username, food_name, expiry):
        add_food(username, food_name, expiry)

    @classmethod
    def delete_food(cls,username, food_name):
        delete_food(username, food_name)

    @classmethod
    def get_expiry_date(cls, username, food_name):

