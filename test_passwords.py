from passwords import User
import unittest

class TestPasswords(unittest.TestCase):
    def setUp(self):
        """
        setUp method to run before each testcase
        """

        self.new_user = User('devjaymmy', 'devjaymmy@2022')

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

if __name__ == "__main__":
    unittest.main()