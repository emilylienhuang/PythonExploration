#Emily Ng

import pprint

def main():
    string = "It was a bright cold day in April, and the clocks were striking thirteen."
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # find and print the most used character and its occurences not including puncuation of white spaces
    dictionary1 = {}

    #count up characters:

    for i in string:
        if not i.isspace() and not i in punctuations:
            if i in dictionary1:
                # add one to the value
                dictionary1[i] += 1
            else:
                # create the key value pair
                dictionary1[i] = 1

    #calculate the most occurring character
    char_most = ''
    count_most = 0

    for key,value in dictionary1.items():
        if count_most <= value:
            char_most = key
            count_most = value

    print("The most occurring character is: " + char_most)

    #count the total number of words
    for i in string:
        if i in punctuations:
            #get rid of punctuation
            string = string.replace(i, "")
    words = string.split()

    print("The word count is: " + str(len(words)))

main()