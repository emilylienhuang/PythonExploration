'''
Homework 2, Exercise 4 Part 1
Emily Ng
2/7/2023
In this exercise part 1 I develop a guess a number game.
I randomly generate a number between 1 and 20 inclusive, then the player has to guess it within 10 tries.
'''

def main():

    #random number between 1 and 20 inclusive
    import random
    num = random.randint(1,20)

    print(num)

    #user will get to guess ten times
    guess_num = 1

    while guess_num <= 10:
        #run until the user runs out of guesses or they guess the number
        user_ans = int(input('Take a guess. \n'))

        if(user_ans < num):
            print("Your guess is too low.")
        elif (user_ans > num):
            print('Your guess is too high.')
        else:
            print('Good job! You guessed my number in ' + str(guess_num) + " guesses!")
            break
        guess_num += 1
    print('Sorry, the number I was thinking of was ' + str(num))

main()