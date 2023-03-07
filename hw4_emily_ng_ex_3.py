'''
Homework 4 Exercise 3
Emily Ng
3/5/2023
This program is a strong password checker
'''

import re

def main():
    print("Create a strong password!")
    print("Password must be at least 8 characters long")
    print("Password must contain both upper and lowercase letters")
    print("Password must contain at least one digit" + "\n")

    password = input("Enter desired password: ")

    '''
    From the beginning of the string, is there at least one lowercase character,
    one uppercase character, and a digit? And is the whole summation of that combination 
    at least 8 characters long?
    '''
    password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


    if password_regex.search(password):
        #print if a match is found
        print("Password is valid!")
    else:
        #wah- waaaaah
        print("Invalid entry.")

main()