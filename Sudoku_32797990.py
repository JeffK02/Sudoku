"""
Template for Programming Assignment FIT1045 - S2 2021
Sudoku

Version 3 (2021-09-22) - containing reference solutions for Part 1

Sudoku boards partially retrieved from
- https://puzzlemadness.co.uk
- https://sudokudragon.com
"""

########### Sudoku boards ##############################

small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudokus = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]

########### Module functions ###########################

from math import sqrt
from typing import Counter

symbols = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

def print_board(board, hint=None):
    """
    Prints a given board to the console in a way that aligns the content of columns and makes
    the subgrids visible.

    Input : a Sudoku board (board) of size 4x4, 9x9, or 16x16,
            optionally the coordinates of a field where to display the hint symbol ('*')
    Effect: prints the board to the console 

    For example:

    >>> print_board(small2)
    -------
    |  |1 |
    |4 |  |
    -------
    |  | 2|
    | 3|  |
    -------
    >>> print_board(big)
    -------------
    |   |   |   |
    |4  |789|   |
    |78 |   | 56|
    -------------
    | 2 |36 |8  |
    |  5|  7| 1 |
    |8  |2  |  5|
    -------------
    |  1|64 |97 |
    |   |9  |   |
    |   | 3 |  2|
    -------------
    >>> print_board(giant2)
    ---------------------
    | 5  | 4 8| 6  |  9G|
    |1   |   D|4  7|F 8 |
    |D   | 73 |   9|5A  |
    | BCF|A   |  5 |34 D|
    ---------------------
    |F 13|  72|    | 5  |
    |   C| 3 5| B E|   9|
    |47  |    |C FG|    |
    |    |E F |69  |  C |
    ---------------------
    |3 F4| DE |   1|  78|
    |    |    |  9A|    |
    |B GA|    | 7  | 35 |
    |  D |    |E GF| 9 1|
    ---------------------
    |9 2 | E 4|8   |    |
    | E  |   A|9 3 |  17|
    |8   |G  1|2EB4|   3|
    |   1|  5 | G 6| C  |
    ---------------------
    """
    n = len(board)
    k = round(sqrt(n))
    for i in range(n):
        if i % k == 0:
            print('-'*(len(board)+k+1))
        for j in range(n):
            if j % k == 0:
                print('|', end='')
            if hint and hint[0]==i and hint[1]==j:
                print('*', end='')
            else:
                print(symbols[board[i][j]], end='')
        print('|')
    print('-'*(len(board)+k+1))

def subgrid_values(board, r, c):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that are present in the subgrid of the board related to the
            field (r, c)

    For example:

    >>> subgrid_values(small2, 1, 3)
    [1]
    >>> subgrid_values(big, 4, 5)
    [3, 6, 7, 2]
    >>> subgrid_values(giant2, 4, 5)
    [7, 2, 3, 5, 14, 15]
    """
    n = len(board)
    k = round(sqrt(n))
    res = []
    for i in range((r // k) * k, ((r // k) + 1) * k):
        for j in range((c // k) * k, ((c // k) + 1) * k):
            if board[i][j]:
                res.append(board[i][j])
    return res 


def options(board, r, c):
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that player is allowed to place on field (r, c),
            i.e., those that are not already present in row r, column c,
            and subgrid related to field (r, c)

    For example:

    >>> options(small2, 0, 0)
    [2, 3]
    >>> options(big, 6, 8)
    [3, 8]
    >>> options(giant2, 1, 5)
    [2, 5, 6, 9, 11, 12, 16]
    """
    if board[r][c]:
        return []

    res = []
    n = len(board)
    k = round(sqrt(n))    
    col_vals = [board[s][c] for s in range(n)]
    row_vals = board[r]
    subgrid_vals = subgrid_values(board, r, c)
    for x in range(1, n+1):
        if x not in col_vals and x not in row_vals and x not in subgrid_vals:
            res.append(x)
    return res

def empty_fields(board):
    """
    Input : Sudoku board
    Output: list of fields, i.e., pairs of row and column indices, that are not
            empty (i.e., value is not equal to 0)
    """
    n = len(board)
    k = int(sqrt(n))
    res = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                res.append((i, j))
    return res

def hint(board):
    """
    Input : Sudoku board
    Output: field, i.e., pair of row and column index, with the minimum
            number of options among all empty-fields

    Hints are generated based in the number of available options for a field.
    Fields with less options are easier to fill for the player, hence, pointing
    to the minimum makes a useful hint.
    """
    fields = empty_fields(board)
    if not fields:
        return None
    min_field = fields[0]
    min_options = len(options(board, fields[0][0], fields[0][1]))
    for i, j in fields[1:]:
        opts = options(board, i, j)
        if len(opts) < min_options:
            min_field = (i, j)
            min_options = len(opts)
    return min_field

from copy import deepcopy

def play(board):
    """
    Input : Sudoku board
    Effect: Allows user to play board via console
    """
    boards = [board]
    print_board(boards[-1])
    while True:
        if not empty_fields(boards[-1]):
            print('solved')
        inp = input().split(' ')
        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():
            i = int(inp[0])
            j = int(inp[1])
            x = int(inp[2])
            opt = options(boards[-1], i, j)
            if x in opt:
                boards.append(deepcopy(boards[-1]))
                boards[-1][i][j] = x
                print_board(boards[-1])
            else:
                print('invalid move; valid options:' + str(opt))
        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            k = int(inp[1])
            d = int(inp[2])
            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                boards = [sudokus[k][d-1]]
                print_board(boards[-1])
            else:
                print('board not found')
        elif inp[0] == 'q' or inp[0] == 'quit':
            return
        elif inp[0] == 'u' or inp[0] == 'undo':
            if len(boards) > 1:
                boards = boards[:-1]
                print_board(boards[-1])
            else:
                print('nothing to undo')
        elif inp[0] == 'r' or inp[0] == 'restart':
            boards = boards[:1]
            print_board(boards[-1])
        elif inp[0] == 'h' or inp[0] == 'help':
            hnt = hint(boards[-1])
            print_board(boards[-1], hint=hnt)
            print(hnt, options(boards[-1], hnt[0], hnt[1]))
        elif inp[0] == "i" or inp[0] == "infer":
            print_board(inferred(boards[-1]))
        elif inp[0] == "s" or inp[0] == "solve":
            back_solve(boards[-1])
        elif inp[0] == "g" or inp[0] == "generate":
            if int(inp[1]) > 1 and int(inp[1]) <= 4:
                a = emp_board(int(inp[1]))
                a = genarator(a)
                new = deepcopy(a)
                boards.append(unique(new))
                print_board(boards[-1])
            else:
                print("Invalid size")
        else:
            print('Invalid input')

########### Functions for Part II ########

def value_by_single(board, i, j):
    """
    Input : board, row, and column index
    Output: The correct value for field (i, j) in board if it can be inferred as
            either a forward or a backward single; or None otherwise. 
    
    For example:

    >>> value_by_single(small2, 0, 1)
    2
    >>> value_by_single(small2, 0, 0)
    3
    >>> value_by_single(big, 0, 0)
    """
    n = len(board)
    k = int(sqrt(n))
    a = options(board,i,j)
   
    if len(a) == 1:
        return a[0]
    else:
        for num in a:
            count = 0
            for row in range(n): #backward single row
                if row == i:
                    continue
                if board[row][j] == 0 and num in options(board,row,j):
                    count += 1
            if count == 0:
                return num

        for num in a:
            count = 0
            for col in range(n): #backward single column
                if col == j:
                    continue
                if board[i][col] == 0 and num in options(board,i,col):
                    count += 1
            if count == 0:
                return num

        for num in a: #backward single subgrid
            count = 0
            for subr in range(i//k*k, i//k*k+k):
                for subc in range(j//k*k, j//k*k+k):
                    if subr == i and subc ==j:
                        continue
                    if board[subr][subc] == 0 and num in options(board,subr,subc):
                        count += 1
            if count == 0:
                return num
        return
           

def inferred(board):
    """
    Input : Sudoku board
    Output: new Soduko board with all values field from input board plus
            all values that can be inferred by repeated application of 
            forward and backward single rule

    For example board big can be completely inferred:

    >>> inferred(big) # doctest: +NORMALIZE_WHITESPACE
    [[2, 1, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [1, 2, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]]

    But function doesn't modify input board:

    >>> big # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 7, 8, 9, 0, 0, 0],
     [7, 8, 0, 0, 0, 0, 0, 5, 6],
     [0, 2, 0, 3, 6, 0, 8, 0, 0],
     [0, 0, 5, 0, 0, 7, 0, 1, 0],
     [8, 0, 0, 2, 0, 0, 0, 0, 5], 
     [0, 0, 1, 6, 4, 0, 9, 7, 0],
     [0, 0, 0, 9, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 0, 0, 2]]

    In board big4 there is nothing to infer:
    
    >>> inferred(big4) # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 6, 0, 0, 2, 0, 0],
     [8, 0, 4, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 9, 0, 0, 0], 
     [4, 0, 5, 0, 0, 0, 0, 0, 7],
     [7, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 0, 5, 0, 0, 0, 8],
     [3, 0, 0, 0, 7, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 1, 9, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 6, 0]]
    """
    infer_board = deepcopy(board)

    def check(board1):
        for i in range(len(board1)):
            for j in range(len(board1)):
                if value_by_single(board1,i,j) != None:
                    return True
        return False
    
    while check(infer_board):
        for i in range(len(infer_board)):
            for j in range(len(infer_board)):
                if value_by_single(infer_board,i,j) != None:
                    infer_board[i][j] = value_by_single(infer_board,i,j)
                
    return infer_board

def back_solve(board):
    """
    At first when any board is passed to this function i use inferred function first,
    then i check whether it is fully inferred or not if yes which means there is no more empty fields,
    it will straight print the board and return True.
    If not i will try to put every option of the stating point and test whether it is the correct answer or not by calling the function recursively.
    If the first option i try does not work and i will reset the field to 0 and try the other options until there isnt any left.
    If every option does not work i will return false which means the sudoku is unsolvable.
    """
    bt_board = inferred(board) # try if the board can be fully inferred or not

    """
    To find the best place to start i use the hint function for this one as i know this function will always give the easiest field for user to start his game
    as this field will have lesser options so it will reduce the computational complexity.
    """
    if hint(bt_board) != None:
        i,j = hint(bt_board)[0],hint(bt_board)[-1] #find the best location to start
    else:
        print_board(bt_board) #when the sudoku is solve print the board for user to inspect
        return True
        
    for opt in options(bt_board,i,j):
        bt_board[i][j] = opt
        if back_solve(bt_board):
            return True
        bt_board[i][j] = 0 #reset the field
    return False #for unsolvable sudoku

from random import choice, shuffle

def emp_board(k):
    """
    a straight forward function to genarate an empty k**2×k**2 Sudoku board
    """

    s = k**2
    opt_list = list(range(1,s + 1))
    new_board = []

    for i in range(s):
        temp = [0]*s
        new_board.append(temp)

    return new_board

def genarator(board):
    
    def checki(board): #when it is fully filled return True
        for row in board:
            if 0 in row:
                return False
        return True
        
    return emp_solver(board,checki) 

def emp_solver(board, func, temp=[]):
    """
    At every iteration i will use inferred to check whether the board can be fully inferred or not to reduce computational time.
    then i will use hint function to find the best spot to start filling the sudoku and list out the options of that particular place and shuffle it.
    After that i will fill the field with available option recursively to check whether which one is the correct solution.
    If after trying all options and none of it is working it will return False which means the sudoku is unsolvable.
    If it is solved every field has its own number, the checki function will return True so the board will be added to temp and return it.
    """
    board = inferred(board)

    if func(board):
        temp.append(board)
        return board

    i,j = hint(board)[0],hint(board)[-1]

    opt_list = options(board,i,j)
    shuffle(opt_list)

    for opt in opt_list:
        board[i][j] = opt
        if genarator(board):
            return temp[-1]
        board[i][j] = 0
    return False

def unique(board):
    """
    i passed through the generated board into it and use a temp to deepcopy it to check afterwards.
    At first i add all the location of the field to a list as tuple and shuffle it.
    After that the list will contains every location of the sudoku board randomly.
    Then i loop through the location list and making the field become zero and check if i am able to get back the original solved board or not(for each locaation i will. check n times).
    If after n times of checking i still get the same board i will proceed to the next location. If not, i set the location back to its original value and try the other location.
    After all location tested, it will return the board with some of the location becomes zero and still after solving it will be the same as the original board.
    """
    if len(board) == 4**2:
        n = 2
    else:
        n = 3
    temp = deepcopy(board)
    choice = []

    for i in range(len(board)):
        for j in range(len(board)):
            choice.append((i,j))
    shuffle(choice)
    
    for ran in choice:
        val = board[ran[0]][ran[-1]]
        board[ran[0]][ran[-1]] = 0
        for i in range(n):
            if genarator(board) != temp:
                board[ran[0]][ran[-1]] = val
                break #if the test failed reset the value and try the others 
    return board

########## Driver code (executed when running module) #

# import doctest
# doctest.testmod()

play(big)
# from random import randint

def frame(h, w):
    for i in range(h):
        if i==0 or i == h-1:
            print("#"*w)
        else:
            for j in range(w):
                if j==0:
                    print("#", end="")
                elif j==w-1:
                    print("#")
                else:
                    print(".", end="")

# frame(6,10)
change_name = { 'A':'.-', 'B':'-...',

                    'C':'-.-.', 'D':'-..', 'E':'.',

                    'F':'..-.', 'G':'--.', 'H':'....',

                    'I':'..', 'J':'.---', 'K':'-.-',

                    'L':'.-..', 'M':'--', 'N':'-.',

                    'O':'---', 'P':'.--.', 'Q':'--.-',

                    'R':'.-.', 'S':'...', 'T':'-',

                    'U':'..-', 'V':'...-', 'W':'.--',

                    'X':'-..-', 'Y':'-.--', 'Z':'--..',

                    '1':'.----', '2':'..---', '3':'...--',

                    '4':'....-', '5':'.....', '6':'-....',

                    '7':'--...', '8':'---..', '9':'----.',

                    '0':'-----'}

# print(MORSE_CODE_DICT['a'.upper()])