'''
Homework 3, Exercise 1
Emily Ng
2/18/2023
This exercise prints a grid image based off an existing gird
'''

def main():
    #The intitial grid:
    grid = [['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

    #the loop:

    for i in range(len(grid[0])):
        #indexing through the columns
        string = '' #collecting the characters per line
        for j in range(len(grid)):
            #indexing through the rows
            string += grid[j][i]
        print(string)


main()