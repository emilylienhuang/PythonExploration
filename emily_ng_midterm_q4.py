#Emily Ng

import random


def main():

    #generate random number between 1 and 10 inclusively
    n = random.randint(1,10)
    print(n)


    square_counter = 0 #stores the count of squares
    i = 0 #index

    while square_counter < n:
        #look at squares
        square = i * i
        if (square % 3 != 0):
            #if square not divisible by 3 print it
            print(square, end = ' ')
            square_counter += 1
        i += 1


main()

