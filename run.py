#!/usr/bin/env python3.6
from user import User
from  credentials import Credential

def create_user(user_name, password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user(user)

def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_user(name)

def existing_users(username,password):
    '''
    Function that check if a user exists with that user and return a Boolean
    '''
    check_user = User.user_exist(username, password)
    return check_user

def display_users():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()

def generate_password(self):
    '''
    Fucntioin that generates password.
    '''
    gen_password = Credential.generate_password(self)
    return gen_password

def create_credential(user_name,sitename,password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credential(user_name,sitename,password)
    return new_credential
def find_by_sitename(sitename):
    '''
    Function that searches for a site name.
    '''
    return Credential.find_by_sitename(sitename)

def save_credential(credential):
    '''
    Function to save a newly created credential.
    '''
    Credential.save_credential(credential)

def check_existing_credentials(sitename):
    '''
    Function that checks if a credential exists.
    '''
    return Credential.credential_exist(sitename)

def copy_credential(sitename):
    '''
    Function that copies credentials details to the clipborad.
    '''
    return Credential.copy_credential(sitename)


def display_credentials(username):
    '''
    Fucntion to display credentials saved.
    '''
    return Credential.display_credential(username)

#Main function
def main():
    print("PASSWORD MANAGER... Welcome")
    while True:
        print("What would you like to do? \n cre - Create Account, log - login, exi - exit the program")
        short_code = input().lower()
       
        if short_code == "cre":
            print('\n')
            user_name = input("Enter your user name:")
            password = input("Type your password:")
            save_user(create_user(user_name,password))
            print(f"Account has been created for {user_name }")
        elif short_code == "exi":
                        break    
            
        elif short_code == "log":
            print('\n')
            print("Enter your login details")
            user_name = input("Enter your user name:")
            password = input("Type your password:")
            exist = existing_users(user_name, password)
            if exist == user_name:
                print(f"You are succesfully logged in {user_name}")
                while True:
                    print("Navigation codes: \n crec - create credential, \n disc - display credential, \n fidc - find credential, \n copc -copy credential \n ext - exit")
                    short_code = input('select a choice: ').lower()
                    if short_code == "ext":
                        break  
                    elif short_code == "crec":
                        print("Enter your credential details")
                        sitename = input("Enter site: ")
                        user_name = input("Enter username: ")
                        create_credential(user_name,sitename,password)
                        save_credential(create_credential(user_name,sitename,password))
                        while True:
                                print("Choose the password method you would like. Use keys: \n ep - To enter a password \n gp - To generate a password \n ex - exit")
                                password_choice = input("Enter an option: ").lower().strip()
                                if password_choice == "entp":
                                    print('\n')
                                    password = input("Enter your password:").strip()
                                    break
                                elif password_choice == "genp":
                                    password = generate_password(password)
                                    break
                    elif short_code == "disc":
                        if display_credentials(user_name):
                            print("This is  a list of all your credentials:")
                            for credential in display_credentials(user_name):
                                print(f"Site name: {credential.sitename} - user name: {credential.username} - Password: {credential.password}")
                        else:
                            print("You dont seem to have any credentials saved")

                    elif short_code == "fidc":
                        search_site = input("Type the site name you are looking for:")
                        if existing_users(user_name,password):
                            result = find_by_sitename(search_site)
                            print(f"Search result: Site: {result.sitename} - username: {result.username} - Password: {result.password}") 
                        else:
                            print("No such credential exists. Try again!")
                    
                    elif short_code == "copc":
                        the_site = input("Enter the site name for the credential you want to copy: ")
                        copy_credential(the_site)
                    
if __name__ == '__main__':
    main()
