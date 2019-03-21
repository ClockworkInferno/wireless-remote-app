#reset password

import os
import getpass
import sys
#import MySQLdb

def resetpassword():
    passwordOk =0
    print("enter your current password: ")
    oldPassword = getpass.getpass()
    
    #check this password with password with database

    while passwordOk == 0:
        print("please enter a password that is at least 8 character and then confirm the password: \n" )
        password = getpass.getpass()
        confirmPassword = getpass.getpass()
        passwordOk = checkPassword(password,confirmPassword)
        if passwordOk == 1:
            break

    print("Password has been reset")
    
def  checkPassword(str1,str2):
    if len(str1) < 8 :
        print("password is not long enough")
        return 0
    if str1 != str2 :
        print("Passwords do not match")
        return 0

    return 1

#main
ans=input("Would you like the reset your password? (y or n) ")
if ans =='y':
    resetpassword()


elif ans=='n':
    print("ok, goodbye")

else:
    print("invalid input")
