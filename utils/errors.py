class UsernameAlreadyExistsError(Exception):
    #raised them the user already exists
    pass

class DatabaseConnectionError(Exception):
    #raised when there is a problem with the database
    pass

class EmailAlreadyExistsError(Exception):
    #raised when the email already exists
    pass