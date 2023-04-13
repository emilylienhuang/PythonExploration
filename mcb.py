'''
Homework 6 Exercise 3
Emily Ng
4/9/2023
This is a python program that saves multiple pieces of text
at a time from a clipboard
'''


import shelve, pyperclip, sys

#create shelf
mcb_shelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    #save text in our dictionary shelf
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print("Text copied to clipboard", sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        #print all key words available
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print(list(mcb_shelf.keys()))
    elif sys.argv[1] in mcb_shelf:
        #copy information from clipboard
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print("clipboard has copied your original clipboard paste at the ready.")
elif len(sys.argv) == 1:
    pyperclip.copy(sys.argv[0])
    #otherwise if only one keyword is provided and no 'save' or 'list' is in the args, the text saved under this keyword is copied to the clipboard?
mcb_shelf.close()