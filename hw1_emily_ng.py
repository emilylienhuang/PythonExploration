"""
Homework 1
Name: Emily Ng
Date: 9/2/22
This program asks the user 3 creative security questions.
After correct responses, it will print a bit of secret information.
The program uses mathematical operators, truthy and falsy values,
while and for loops, and functions such as input, str, int, and randint.
The answers for the security questions are as follows:
1. It depends, will be defined in the function and marked with a variable identifier
    However, birth year is 1998 and age is 24. Don't call me old.
2. Lienhua
3.Jade
"""


import random


def user_validation_number(question, user_input_num, expected_num):
    user_correct = False
    while not user_correct:
        if user_input_num != expected_num:
            print('Incorrect number. Try again.')
            print(question)
            user_input_num = input()
            while "." in user_input_num:
                print('You didn\'t listen. No decimals. Try again.')
                print(question)
                user_input_num = input()
            user_input_num = int(user_input_num)
        else:
            user_correct = True


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
            user_correct = True


def main():
    # We will ask three questions using a for loop
    for i in range(3):
        if i == 0:
            # Here we are asking question 1 which will have a numeric result
            random_divisor = random.randint(1, 100)
            question_1 = 'Enter your ((birth year * your age)/' + str(random_divisor) + ') - 2 without decimal values: '
            print(question_1)
            response = input()  # user response taken in a s a float for error handling
            while "." in response:  # check if user has entered a decimal number
                print('You don\'t listen. No decimals. Try again.')
                question_1 = 'Enter your ((birth year * your age)/' + str(
                    random_divisor) + ') - 2 without a remainder: '
                print(question_1)
                response = input()
            response = int(response)
            result = ((1998 * 24)//random_divisor) - 2  # answer to question_1
            user_validation_number(question_1, response, result)  # will validate the user input
        elif i == 1:
            # moves on to question 2 asking user to enter their middle name.
            middle_name = 'LIENHUA'
            question_2 = 'What is your middle name?'
            print(question_2)
            user_middle_name_entry = input()
            user_middle_name_entry = user_middle_name_entry.upper()  # making sure user input is not influenced by case
            user_validation_string(question_2, user_middle_name_entry, middle_name)
        else:
            # moves on to question 3 asking user to enter their favorite plant
            plant_name = 'JADE'
            question_3 = 'What is your favorite plant?'
            print(question_3)
            user_plant_entry = input()
            user_plant_entry = user_plant_entry.upper()  # making sure user input is not influenced by case
            user_validation_string(question_3, user_plant_entry, plant_name)
    print('Secret Message: I\'m wait listed for CS3080, but I want to be in the course. Not a good position.')


main()
