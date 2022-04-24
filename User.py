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
        method adds existing credentials of user
        """

        self.website_address = website_address
        self.username = username
        self.password = password

    


        

    