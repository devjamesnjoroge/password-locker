import string
import random


class User:

    """
    Creates a user class for our password locker account.                                                
    """

    user_list = []

    """
    Creates an empty users List
    """

    def __init__(self, username, password):

        """
        Creates an instance of users username and password
        """

        self.username = username
        self.password = password
    
    def save_User(self):

        """
        Save_User method save User objects into user_list
        """

        User.user_list.append(self)


class Credentials:

    """
    Creates a credentials class for the users multiple accounts
    """

    def __init__(self, website_address, username, password):

        """
        Initializes parameters to our class credentials
        """

        self.website_address = website_address
        self.username = username
        self.password = password

    def add_existing_credentials(self, website_address, username, password):

        """
        method adds existing credentials of user for already existing accounts
        """

        self.website_address = website_address
        self.username = username
        self.password = password

    def create_new_credentials(self, website_address, username, password):

        """
        method enables user to create new credentials for a new account
        """

        self.website_address = website_address
        self.username = username
        self.password = password
    
    def generatePassword(string_length=12):
        """
        Generate a random password string of letters and digits and special characters
        """
        password_list = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*?/|"
        return ''.join(random.choice(password_list) for i in range(string_length))



        

    