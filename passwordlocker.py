from user import User
from credentials import Credentials


def create_user(username, password):
    # '''
    # Function to create a new user
    # '''

    new_user = User(username, password)
    return new_user
