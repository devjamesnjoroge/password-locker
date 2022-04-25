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

    def __init__(self, website, username, password):

        """
        Initializes parameters to our class credentials
        """

        self.website = website
        self.username = username
        self.password = password
    
    def generatePassword(string_length=12):
        """
        Generate a random password string of letters and digits and special characters
        """
        password_list = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*?/|"
        return ''.join(random.choice(password_list) for i in range(string_length))

    credentials_dict = []


    def save_credentials(self):
        """
        saves newly added credentials to the list
        """
        Credentials.credentials_dict.append(self)

    def delete_credentials(self):
        """
        Deletes saved credentials in list
        """

        Credentials.credentials_dict.remove(self)

    @classmethod
    def find_by_website(cls,website):
        '''
        Method that takes in a website and returns a credential that matches that website.

        Args:
            number: Website to search for
        Returns :
            credentials of account that matches the website.
        '''

        for credential in cls.credentials_dict:
            if credential == website:
                return credential
            else:
                return credential
            