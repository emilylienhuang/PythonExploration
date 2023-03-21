'''
Homework 5, Exercise 2
Emily Ng
3/14/2023
In this exercise, we used a generator function to find the first n pythagorean triplets
'''

import numpy as np

def pythagoreanTriplets(num_triplets):
    c = 0
    m = 1
    count = 0

    #formula for pythagorean triples from  https://www.chilimath.com/lessons/geometry-lessons/generating-pythagorean-triples/
    # m > n   where m and n are positive integers
    #a = m^2 - n^2
    #b = 2mn
    #c = n^2 + m^2

    # Limiting c would limit
    # all a, b and c
    while count < num_triplets:
        # Now loop on n from 1 to m-1 must start at 1 bc 0 is neither positive nor negative
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if we reached the necessary number
            if count > num_triplets:
                break
            else:
                count += 1
                yield (a,b,c)

        m = m + 1


def main():
    n = input('Number of triples required: ')
    call = pythagoreanTriplets(int(n))

    print(list(call))  #print out the list of triples

main()
