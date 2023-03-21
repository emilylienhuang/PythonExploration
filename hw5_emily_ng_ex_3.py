'''
Homework 5, Exercise 3
Emily Ng
3/14/2023
In this exercise, we used a generator function to perform the same tasks as range
'''



#unlimited function arguments - partay!
def genrange(*args):
    if len(args) == 1:
        #only argument is stop
        i = 0
        while i < args[0]:
            yield i
            i += 1
        return
    elif len(args) == 2:
        #start and stop arguments
        start = args[0]
        stop = args[1]
        i = start
        while i < stop:
            yield i
            i += 1
        return
    else:
        #start,stop, and step arguments
        start = args[0]
        stop = args[1]
        step = args[2]
        i = start
        while i < stop:
            yield i
            i += step
        return


def main():
    print("One arg genrange:")
    call1 = genrange(11)
    for i in call1:
        print(i, end = " ")

    print()

    print("two arg genrange:")
    call2 = genrange(0,11)
    for i in range(10):
        print(next(call2), end = " ")

    print()

    print("Three arg gen range:")
    call3 = genrange(0,11,2)
    for i in call3:
        print(i, end = " ")


main()