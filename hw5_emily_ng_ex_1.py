'''
Homework 5, Exercise 1
Emily Ng
3/14/2023
In this exercise, we created a reverse iterator to traverse a list
'''

class ReverseIter():
    def __init__(self, l):
        #initialize a list and its index value
        self.list = l
        self.index = len(l)

    def __iter__(self):
        #return the iterator
        return self

    def __next__(self):
        if self.index <= 0:
            #stop iteration if past the beginning of the list
            raise StopIteration
        else:
            #returning the items in reverse order
            self.index = self.index -1
            return self.list[self.index]


def main():
    #call to test
    it = ReverseIter([1,2,3,4])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
main()
