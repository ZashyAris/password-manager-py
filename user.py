class user:
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
        
        