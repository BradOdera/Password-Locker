from user import User
from credentials import Credentials


def create_user(username, password):

    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    function to save user
    '''

    User.save_user(user)
