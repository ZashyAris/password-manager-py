import pyperclip
import random 
import string
class Credential:
  '''
  class that generates new credentials
  '''
  credential_list = [] # an empty list

  def __init__(self,username,sitename,password):
    self.username = username
    self.password = password
    self.sitename = sitename

  def save_credential(self):
    '''
    save_cred method saves the user objects into creds_list
    '''
    Credential.credential_list.append(self)

  @classmethod
  def display_credential(cls, user_name):
    '''
    Class method to show the list of credentials saved
    '''
    users_credential_list = []
    for credential in cls.credential_list:
        if credential.username == user_name:
          users_credential_list.append(credential)
        return users_credential_list

  def delete_credential(self):
    '''
    delete_contact method deletes a saved credential from the credential_list
    '''
    Credential.credential_list.remove(self)

  def generate_password(self):
         '''
         Function to generate a password where a user can generate a password based on their length of choice
         '''
         chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
         password = ""

         print("Use Char list = %s \n" % chars)

         length = int(input("[*] Input Password Length: "))
         while len(password) != length:
             password = password + random.choice(chars)
             if len(password) == length:
                 print("Password: %s" % password)
         return password
  @classmethod
  def find_by_sitename(cls, sitename):
      '''
      Class method that takes a site name and returns the credential that matches that site
      '''
      for credential in cls.credential_list:
          if credential.sitename == sitename:
              return credential
  
  @classmethod
  def credential_exist(cls, sitename):
    '''
    Method that checks if user exists from the credential list.
    Returns:
    Boolean: True or false depending if the credential exits
    '''
    the_credential = ""
    for credential in Credential.credential_list:
      if (credential.sitename == sitename):
        the_credential = sitename
    return the_credential

  @classmethod
  def copy_credential(cls, sitename):
      '''
      Class method that copies a credentials details after the credentials sitename has been entered
      '''
      find_credential = Credential.find_by_sitename(sitename)
      return pyperclip.copy(find_credential.password)