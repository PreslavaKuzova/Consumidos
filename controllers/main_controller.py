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

if __name__ == '__main__':
    main()