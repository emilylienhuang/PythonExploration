'''
Homework 2, Exercise 2
Emily Ng
2/7/2023
In this exercise, I write a function named collatz that has one
argument called number. If the number is even, I print the result of integer division.
If the number is odd, I print the number times 3 plus 1. This exercise uses try and except
statements.
'''

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


def main():

    try:
        number = int(input("Enter a number: "))  # collect user input
        while True:
            #will ask user for number until the resultant number equals 1
            number = collatz(number)
            print(number)
            if number == 1:
                break
    except:
        #the user did not enter a number, we will let them know
        print("Bad user! You must enter an integer. ")


main()
