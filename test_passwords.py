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

if __name__ == "__main__":
    unittest.main()