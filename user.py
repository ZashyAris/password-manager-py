class User:
    """
    Class that generates new instance of users
    """

    user_list = [] # Empty user list
    
    def __init__(self,user_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New user user_name.
            password: New user password.
        '''

        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
        
    @classmethod
    def find_by_user(cls,user):
        '''
        Method that takes in a name and returns a user that user name .

        Args:
            name: User name to search for
        Returns :
            User of person that matches the user name.
        '''

        for user in cls.user_list:
            if user.user_name == user:
                return user
            
    @classmethod
    def user_exist(cls,user, password):
        '''
        Method that checks if a user name exists from the user list.
        Args:
            name: User name to search if it exists
        Returns :
            Boolean: True or false depending if the user name exists
        '''
        user = ''
        for user in User.user_list:
            if(user.user_name == user and user.password == password):
                user = user.user_name
                return User

        return False
    
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
        