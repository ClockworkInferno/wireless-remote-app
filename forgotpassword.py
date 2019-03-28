#Clancy
#forgotpassword

import os
import getpass
import sys

def forgotpassword():
    passwordOk =0
    email=input("enter your current email address: ")
    
    #check this email with account email
    print("For this test to simulate reseting password, the code which would be sent you your email is 1234")
    code=input("enter code that was sent to your email: ")

    if code == "1234":
        while passwordOk == 0:
            print("please enter a password that is at least 8 character and then confirm the password: \n" )
            password = getpass.getpass()
            confirmPassword = getpass.getpass()
            passwordOk = checkPassword(password,confirmPassword)
            if passwordOk == 1:
                break

        print("Password has been reset")
    else:
        print("code is invalid")


def  checkPassword(str1,str2):
    if len(str1) < 8 :
        print("password is not long enough")
        return 0
    if str1 != str2 :
        print("Passwords do not match")
        return 0

    return 1


ans=input("did you forget you password? (y or n) ")
if ans =='y':
    forgotpassword()
    
elif ans=='n':
    print("ok, goodbye")

else:
    print("invalid input")
