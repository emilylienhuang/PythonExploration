'''
Homework 6, Exercise 1
Emily Ng
4/3/2023
This is a slow down decorator function. Code modified from given real world
decorator examples in class
'''
import functools
import time

#optional sleep time argument
def slowDownWrapperWrapper(original_function = None, sleep_time = None):
    def slowDown(func):
        #sleep with default equal to 1 second
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            if sleep_time is None:
                #if not instantiated sleep time then set to 1
                time.sleep(1)
            else:
                #otherwise call time.sleep with sleep time
                time.sleep(sleep_time)
            return func(*args, **kwargs) #return the result of the function with the given arguments
        return wrapperSlowDown
    if original_function:
        #if the original function is defined call slow down
        return slowDown(original_function)
    return slowDown


#test with half second sleep time
@slowDownWrapperWrapper(sleep_time=0.5)
def countdown(from_num):
    if from_num < 1:
        print("Liftoff!")
    else:
        print(from_num)
        countdown(from_num - 1)

def main():
    countdown(5)
main()

