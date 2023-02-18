'''
Homework 3, Exercise 4
Emily Ng
2/18/2023
This is a tic-tac-toe game.
This program assumes the user enters everything in the correct case
and only valid inputs.
This game does not check for a winner. It will just print the final board.
'''

import random

def printBoard(board):
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|' + board['mid-middle'] + '|' + board['mid-right'])
    print('-+-+-')
    print(board['low-left'] + '|' + board['low-middle'] + '|' + board['low-right'])

def main():
    # Create a dictionary
    board = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ',
                'mid-left': ' ', 'mid-middle': ' ', 'mid-right': ' ',
                'low-left': ' ', 'low-middle': ' ', 'low-right': ' '}


    printBoard(board) #show the empty board

    #players can be X or O
    players = ['X', 'O']


    turn = random.choice(players) #who goes first
    for i in range(9):
        #there are 9 slots on the board we will go until they are filled
        print("Turn for " + turn + ". Which place you want go?")
        print("Your choices are :")
        for j in board.keys():
            #outputting options for non-occupied slots
            if board[j] == ' ':
                print(j)
        move = input("Enter your choice: ")
        board[move] = turn

        #switch players:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        #show the board after a player's turn
        printBoard(board)



main()