import sys
sys.path.insert(0, '/root/Python-101/Consumidos/database')

import queries

class LoginController:
    @classmethod
    def sign_in(cls, username):
        if not queries.sign_in_user(username) is None:
            return queries.get_all_user_products(username)
        else:
            raise 'UserDoesntExist'

if __name__ == '__main__':
    main()