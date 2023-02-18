'''
Homework 3, Exercise 2
Emily Ng
2/18/2023
This exercise returns the number of character occurrences in a string
including letters, punctuations, and white spaces. Letters ARE case sensitive
Storing the results in a dictionary
'''

import pprint

def main():
    string = 'The quick brown fox jumps over the lazy dog.'
    dictionary = {}
    for i in range(len(string)):
            if string[i] in dictionary:
                #add one to the value
                dictionary[string[i]] += 1
            else:
                #create the key value pair
                dictionary[string[i]] = 1
    spam = pprint.pformat(dictionary)
    print(spam)
main()