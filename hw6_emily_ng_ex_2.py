'''
Homework 6, Exercise 2
Emily Ng
4/3/2023
This exercise generates a more efficient fibonnacci sequence
using a cache and a call counter.
'''

#cache decorator definition
def cache(function):
    dictionary = {}
    def wrapper(*args):
        if args in dictionary:
            #if val in the cache already return it
            return dictionary[args]
        else:
            #save val in cache if it doesn't exist yet
            dictionary[args] = function(*args)
            return dictionary[args]
    return wrapper

def countCalls(function):
    def counter(*args, **kwargs):
        #increment the calls attribute everytime counter is called
        counter.calls += 1
        print(counter.calls)
        return function(*args, **kwargs)
    counter.calls = 0
    return counter

print("With Cache:")
@cache
@countCalls
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
fibx = fibonacci(5)
print("With Cache: ", fibx)

print("Without Cache:")
@countCalls
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
fib2 = fibonacci(5)
print("no cache", fib2)

#@countCalls
