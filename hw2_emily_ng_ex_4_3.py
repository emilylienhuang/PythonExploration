'''
Homework 2, Exercise 4 Part 1
Emily Ng
2/7/2023
In this exercise part 1 I develop a guess a number game.
I randomly generate a number with random upper and lower bounds, then the player has to guess it within 10 tries.
The player is now the computer because I guess we are into anarchy now.
'''

def main():

    #random number between 1 and 20 inclusive
    import random
    import sys
    lower_bound = random.randint(-100, 100)
    upper_bound = random.randint(lower_bound, 200)

    num = random.randint(lower_bound, upper_bound)

    print('I am thinking of a number between '+ str(lower_bound) +" and "+ str(upper_bound))

    #user will get to guess ten times
    guess_num = 1

    while guess_num <= 10:
        #keep track of prior guesses
        prior_guesses = []

        #run until the user runs out of guesses or they guess the number
        print('Take a guess.')

        user_ans = random.randint(lower_bound, upper_bound)

        #not going to allow guesses already guessed

        while user_ans in prior_guesses:
            user_ans = random.randint(lower_bound, upper_bound)

        prior_guesses.append(user_ans)

        print(user_ans)

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