from user import User
from credentials import Credentials


def create_user(username, password):
    """
    Function to create a new user
    """

    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    function to save user
    """

    User.save_user(user)


def create_credentials(account, username, password):
    """
    Function to create credentials
    """

    new_credentials = Credentials(account, username, password)
    return new_credentials


def display_credentials(username):
    """
    function that returns all the saved contacts
    """

    return Credentials.display_credentials()


def save_credentials(self):
    """
    function that saves user credentials
    """

    Credentials.save_credentials(self)
