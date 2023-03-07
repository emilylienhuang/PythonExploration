'''
Homework 4 Exercise 2
Emily Ng
3/5/2023
This program is a phone and email address extractor
'''

import re
import pyperclip

def main():

   #take in text from the clipboard
   text_input = pyperclip.paste()

   # text_input = "719-287-7231 mud purple@gmail.com duck" tester to make sure function works

   #strings we will check
   groups_to_check = text_input.split()

   for i in groups_to_check:
      #check for phone number
      phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

      phone_match = phone_num_regex.search(i)

      if phone_num_regex.search(i):
         print(phone_match.group())

      #check for email address
      '''
      whatever string @ some other string . whatever site name with at least 3 characters
      '''
      email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{3,})+')

      email_match = email_regex.search(i)
      if email_regex.search(i):
         print(email_match.group())


main()


