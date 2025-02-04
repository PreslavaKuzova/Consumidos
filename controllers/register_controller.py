import sys
sys.path.insert(0, '/root/Python-101/Consumidos/database')
sys.path.insert(0, '/root/Python-101/Consumidos/utils')
from database.dataBase import *
import database.queries as queries
from utils.errors import *


class RegisterController:
    @classmethod
    def sign_up(cls, username, email):
        if not queries.sign_in_user(username):
            queries.add_new_user(username, email)
        else:
            raise DatabaseConnectionError()