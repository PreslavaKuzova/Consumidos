import sys
sys.path.insert(0, '/root/Python-101/Consumidos/database')

import dataBase
import queries


class RegisterController:

    @classmethod
    def sign_up(cls, username, email):
        if not queries.sign_in_user(username):
            queries.add_new_user(username, email)
            return queries.get_all_user_products(username)
        else:
            raise UserAlreadyExists


if __name__ == '__main__':
    main()