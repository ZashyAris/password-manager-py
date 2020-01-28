import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Zashy", "zashy12345") # create user object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Zashy")
        self.assertEqual(self.new_user.password,"zashy12345")

    User.user_list = [] # Empty user list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("zashy", "zashy12345") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Zashy", "zashy12345") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_find_by_user(self,user_name):
            '''
            test to check if we can find a user  by username and display information
            '''

            self.new_user.save_user()
            test_user = User("Zashy" ,"zashy12345") # new user
            test_user.save_user()

            found_user = User.find_by_user ("Zashy")
            self.assertEqual(found_user.user_name,  test_user.user_name)
            
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Zashy", "zashy12345") # new user
        test_user.save_user()

        user_exists = User.user_exist("Zashy","zashy12345")

        self.assertTrue(user_exists)
    def test_display_all_user(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_user(),User.user_list) 

if __name__ == '__main__':
    unittest.main()