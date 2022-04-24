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

    