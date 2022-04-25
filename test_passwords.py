from passwords import User
from passwords import Credentials
import unittest

class TestPasswords(unittest.TestCase):
    def setUp(self):
        """
        setUp method to run before each testcase
        """

        self.new_user = User('devjaymmy', 'devjaymmy@2022')
        self.new_credentials = Credentials('aws.amazon.com', 'devjaymmy', 'devjaymmy@2022')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_dict = []

    def test_init(self):
       
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, 'devjaymmy')
        self.assertEqual(self.new_user.password, 'devjaymmy@2022')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_User() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_dict),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("aws.amazon.com", "devjaymmy", "devjaymmy@2022") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_dict),2)

    def test_find_credentials_by_website(self):
        '''
        test to check if we can find a credential by website and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("www.example.com", "devjaymmy", "Test@2022") # new credentials
        test_credentials.save_credentials()

        found_website = Credentials.find_by_website("www.example.com")

        self.assertEqual(found_website.username, test_credentials.username )


if __name__ == "__main__":
    unittest.main()