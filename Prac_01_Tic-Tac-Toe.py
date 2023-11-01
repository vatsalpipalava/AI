import numpy as np
import time

board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
players = ['X', 'O']

def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won")
            return True
    return False
        
def check_cols(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won")
            return True
    return False

def check_diagonals(symbol):
    if board[0][2] == board[1][1] == board[2][0] == symbol or board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, "won")
        return True
    return False
        
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
    
def place(symbol):
    while(1):
        row = int(input("Enter row - 1 or 2 or 3: "))
        col = int(input("Enter column - 1 or 2 or 3: "))
        if row > 0 and row < 4 and col > 0 and col < 4 and board[row-1][col-1] == '-':
            break
        else:
            print("Invalid input. Please enter again.")
    board[row-1][col-1] = symbol
    
def play():
    for turn in range(9):
        if turn%2 == 0:
            print("X's turn")
            place(players[0])
            if won(players[0]):
                break
        else:
            print("O's turn")
            place(players[1])
            if won(players[1]):
                break
        print(board)
        
    if not(won(players[0])) and not(won(players[1])):
        print("It's a draw.")

play()