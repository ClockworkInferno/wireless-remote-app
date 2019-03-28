from user import User
from user import RegUser
from loginrepo import *
from registerservice import RegisterService
from loginservice import LoginService

def main():
    
   
    #print("the username is: ", user.username) #prints the username that was provided (checks for now)
    #print("the password is: ", user.password) #prints the password that was provided (checks for now)
    for i in range(2):

        print("this is the 1st iteration of registering users: ", i)
        register_service = RegisterService(LoginAdd())#uses the class RegisterService to gain access to the login repository and add a new user
        reguser = register_service.register_user(input("Enter username: "), input("Enter Password: "), input("Enter Email: "), input("Enter First Name: "), input("Enter Last Name: "))
        print("the username is: ", reguser.username) #prints the username that was provided (checks for now)
        print("the password is: ", reguser.password) #prints the password that was provided (checks for now)
        print("The users name is: ", reguser.fname, reguser.lname) #prints the firstname and lastname of user (checks for now)
        print("the users email is: ", reguser.email) #prints the email of the user (checks for now)
        
    login_service = LoginService(LoginRepo()) #uses to call to LoginRepo class
    user = login_service.login_user(input("Enter username: "), input("Enter Password: ")) #prompts user for username / password
    reg_serv = RegisterService(LoginSearch())
    reg_user = reg_serv.
    print(user.username, user.password)
    print(registeredusers)
   # if user ==
    #        print("success")
    #else:
     #       print("fail")














if __name__ == "__main__": #calls main()
    main()
