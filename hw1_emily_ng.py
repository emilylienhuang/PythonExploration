"""
Homework 1
Name: Emily Ng
Date: 1/26/23
This program asks the user 3 creative security questions.
After correct responses, it will print a bit of secret information.
The program uses mathematical operators, truthy and falsy values,
while and for loops, and functions such as input, str, int, and randint.
The answers for the security questions are as follows:
1. It depends, will be defined in the function and marked with a variable identifier
    However, birth year is 1998 and age is 24. Don't call me old.
2. 31
3.Jade
"""


import random

#this function validates user input, converts input to an integer, and checks to see if the answer is correct
def user_validation_number(question, expected_num):
    user_input_num = ''
    while True:
        print(question)
        user_input_num = input()

        if not user_input_num:
            print('Nothing was entered')
        if not user_input_num.isdecimal():
            print("Must enter a number")
        else:
            user_input_num = int(user_input_num)
            if user_input_num != expected_num:
                print('Incorrect entry. Try again.')
            else:
                break


#this function validates a string
def user_validation_string(question, user_input, answer):
    user_correct = False
    while not user_correct:
        if not user_input:
            print('You did not enter anything. Try again.')
            print(question)
            user_input = input()
            user_input = user_input.upper()
        elif user_input != answer:
            print('Incorrect answer. Please try again.')
            print(question)
            user_input = input()
            user_input = user_input.upper()
        else:
            break


def main():
    # We will ask three questions using a for loop
    for i in range(3):
        if i == 0:
            # Here we are asking question 1 which will have a numeric result
            random_divisor = random.randint(1, 100)
            question_1 = 'Enter your ((birth year * your age)/' + str(random_divisor) +') - 2 rounded down to the nearest integer.'
            result = ((1998 * 24.0) // random_divisor) - 2   # answer to question_1
            if user_validation_number(question_1, result):
                # will validate the user input and continue to the next iteration of the loop
                continue
        elif i == 1:
            # moves on to question 2 asking user to enter the sum of the numbers in their birthday.
            answer = 2 + 2 + 1 + 9 + 9 + 8 #born February, 2, 1998
            question_2 = 'What is the sum of the numbers in your birthday (month, day, year)?'
            if user_validation_number(question_2, answer):
                continue  #will not exectue if there is an error in executing the function
        else:
            # moves on to question 3 asking user to enter their favorite plant
            plant_name = 'JADE'
            question_3 = 'What is your favorite plant?'
            print(question_3)
            user_plant_entry = input()
            user_plant_entry = user_plant_entry.upper()  # making sure user input is not influenced by case
            if user_validation_string(question_3, user_plant_entry, plant_name):
                continue
    print('Secret Message: I am an unfrugal former econ major. I spent $22 on a deoderant that smells like sh*t, and now I have to use a $22 sh*tty deoderant.')


main()
