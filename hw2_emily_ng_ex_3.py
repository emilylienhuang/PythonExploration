'''
Homework 2, Exercise 3
Emily Ng
2/7/2023
In this exercise, I play with a list of things in my purse in various capcities
'''


def main():

    #1. create a list with the strings and print it in one line
    purse_contents = ['Wallet', 'Phone', 'Keys']
    print(purse_contents)

    print()

    #2. sort the list using the sort() function, then print the list again
    purse_contents.sort()
    print(purse_contents)

    print()

    #3. Print the first item in the list
    print(purse_contents[0])

    print()

    #4. print everything but the first item in the list using slicing
    print(purse_contents[1:])

    print()

    #5. Print the last item in the list using a negative index
    print(purse_contents[-1])

    print()

    #6. Print the index of 'Keys' using index()
    print(purse_contents.index('Keys'))

    print()

    #7. Append Tablet to the list then print the list
    purse_contents.append('Tablet')
    print(purse_contents)

    print()

    #8. Insert Mask into the list as the second item then print the list
    purse_contents.insert(1, 'Mask')
    print(purse_contents)

    print()

    #9.Remove 'Phone' from the list and then print it
    purse_contents.remove('Phone')
    print(purse_contents)

    print()

    #10. reverse the list and then print it
    purse_contents.reverse()
    print(purse_contents)

    print()

    #11. Write a function strList that takes the current list and returns all the items separated by a comma and a space and an and before the last item
    def strList(list):
        print(", ".join(list[i] for i in range(len(list))), end = '')
        print(' and ' + list[-1])

    strList((purse_contents))


main()