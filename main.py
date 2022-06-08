# savedata store players location
# player logins

import csv

def intro():    
    print('Welcome to Login Simulator 96')
    print()

def logindetails():
    __logindetails__ = False
    login_account = input('Do you have an account? ')
    print()
    if login_account == 'yes':
        return True
    if login_account == 'no':
        while __logindetails__ == False:
            username = input('What will your username be? ')
            print()
            password = input('What will your password be? ')
            print()
            print("Username:",username,"Password:",password)
            if len(username) > 24:
                print('You cannot have more than 24 characters in your username.')
                xba = False
            elif len(username) < 3:
                print('You must atleast 3 characters in your username.')
                xba = False
            elif len(username) > 2 < 25:
                xba = True
                if xba == True:
                    check_info = input('Are you sure you would like to use these as your login details? ')
                    if check_info == 'yes':
                        __logindetails__ = [username,'\t',password,'\n']
                        with open('accounts.txt', 'a') as f:  
                            f.write(username + '\t' + ':' + '\t' + password + '\n')

def main():
    intro()
    logindetails()

    
main()
