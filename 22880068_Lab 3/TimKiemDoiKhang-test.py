#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)

------
Adapted by Luu Ngoc Khang - HCMUS 22880068
For school project use.

"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def create_board(board_size):
    board = [[0] * board_size for _ in range(board_size)]       
    # This creates a list with many lists of different IDs
    print(board)
    return board

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def get_player_cell_coords(state,player):
    player_cell_coords = []
    for i in range(0, len(state)):          # index of row
        for j in range(0,len(state[i])):    # index of column
            if state[i][j] == player:
                player_cell_coords.append((i,j))  # coordination of cell
    return player_cell_coords

        
"""def horizontal_line_check(cells, player):
    count = 0
    while len(cells) > 0 and count < number_to_win:         # using while to not move the cell index too much
        cell_ref = cells[0].copy()             # get a copy of that cell to increment y
        while count < number_to_win:
            if cell_ref in cells:
                count = count + 1
                cells.remove(cell_ref)
                cell_ref[1] = cell_ref[1] + 1    # increment y
            else:
                count = 0           # reset count
                break               # break from while and get next cell
    if count == number_to_win:
        return True
    else:
        return False"""
    
"""def vertical_line_check(cells,player):
    count = 0
    while len(cells) > 0 and count < number_to_win:         # using while to not move the cell index too much
        cell_ref = cells[0].copy()             # get a copy of that cell to increment y
        while count < number_to_win:
            if cell_ref in cells:
                count = count + 1
                cells.remove(cell_ref)
                cell_ref[0] = cell_ref[0] + 1    # increment y
            else:
                count = 0           # reset count
                break               # break from while and get next cell
    if count == number_to_win:
        return True
    else:
        return False """ 
    
"""def upward_diagonal_line_check(cells,player):
    count = 0
    while len(cells) > 0 and count < number_to_win:         # using while to not move the cell index too much
        cell_ref = cells[0].copy()             # get a copy of that cell to increment y
        
        while count < number_to_win:
            if cell_ref in cells:
                count = count + 1
                cells.remove(cell_ref)
                cell_ref[0] += 1   # x = x + i, y = y - i
                cell_ref[1] -= 1   # because it checks from each row, therefore this has to be downward reverse slash    
            else:
                count = 0           # reset count
                break               # break from while and get next cell
    if count == number_to_win:
        return True
    else:
        return False"""      

"""def downward_diagonal_line_check(cells,player):
    count = 0
    while len(cells) > 0 and count < number_to_win:         # using while to not move the cell index too much
        cell_ref = cells[0].copy()             # get a copy of that cell to increment y
        while count < number_to_win:
            if cell_ref in cells:
                count = count + 1
                cells.remove(cell_ref)
                cell_ref[0] = cell_ref[0] + 1   # x = x + i, y = y + i
                cell_ref[1] = cell_ref[1] + 1   
            else:
                count = 0           # reset count
                break               # break from while and get next cell
    if count == number_to_win:
        return True
    else:
        return False    """

def wins(state, player):
    """
    :param x_count, y_count: de dem ngang doc
    :dl_count, dr_count: dem cheo trai, cheo phai
    :player_cell_coords: toa do cac o cua nguoi choi
    """
    player_cell_coords = get_player_cell_coords(state, player)
    for i in range (0,len(state[0])): # rows
        x_count = 0
        y_count = 0
        for j in range(0, len(state[1])):
            x_count+=1 if (j, i) in player_cell_coords else -x_count
            y_count+=1 if (i, j) in player_cell_coords else -y_count
            if x_count == number_to_win:
                return True
            elif y_count == number_to_win:
                return True
    for x in range(0, len(state[0])):
        for y in range(0, len(state[1])):
            dl_count = dr_count = 1 # diagonal left and diagonal right
            if (x, y) in player_cell_coords:
                for d in range(1, number_to_win):
                    dr_count +=1 if (x + d, y + d) in player_cell_coords else -dr_count
                    dl_count +=1 if (x - d, y + d) in player_cell_coords else -dl_count
                    if dr_count == number_to_win:
                        return True
                    if dl_count == number_to_win:
                        return True
    return False

"""def wins3(state, player): #old codes
    
    player_cell_coords = get_player_cell_coords(state, player)
    
    if horizontal_line_check(player_cell_coords[:], player):
        return True
    if vertical_line_check(player_cell_coords[:], player):
        return True
    if upward_diagonal_line_check(player_cell_coords[:], player):
        return True
    if downward_diagonal_line_check(player_cell_coords[:], player):
        return True
    return False
    
    # 1. Take all player cells
    # 2. Check from cell with four possibilities. If wrong, break.
    # 3. Declare victory"""
    

"""def wins2(state, player): #old codes
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False
"""
def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player, initial_depth, alpha, beta):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    # v0.1: Added initial_depth to limit seeking
    # v0.2: Alpha-Beta pruning: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
    
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]
        
    if depth == 0 or depth < initial_depth-7 or game_over(state): # look forward 3 steps / leaf node
        score = evaluate(state)
        return [-1, -1, score]
    
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player, initial_depth, alpha, beta)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
            if best[2] > alpha[2]:
                alpha = best
            if beta[2] <= alpha[2]:
                break
        else:
            if score[2] < best[2]:
                best = score  # min value
            if best[2] < beta[2]:
                beta = best
            if beta[2] <= alpha[2]:
                break

    return best
""" 
    draft: Old codes
    if player == COMP:
        best = (-1, -1, -infinity)
        for cell in empty_cells(state):
            score = minimax(state, depth - 1, -player, alpha, beta)
            if score[2] > best[2]:
                best = score  # max value
            if best[2] > alpha[2]:
                alpha = best
            if beta[2] <= alpha[2]:
                break
        return best
    else:
        best = [-1, -1, +infinity]
        for cell in empty_cells(state):
            score = minimax(state, depth - 1, -player, alpha, beta)
            best = min(best[2], score[2])
            beta = min(beta[2], best[2])
            if beta <= alpha:
                break


    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player, initial_depth)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
"""

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def render_column_indexes(board):
    l = len(board)
    # in hang chuc
    if l > 9: 
            print("  ", end="")
            count = 0
            # print the first 9 spaces
            for i in range(1,10): 
                print(" ",end="")
            l = l - 9
            # if l is still larger than 10
            while (l > 10): 
                count = count+1
                for i in range(1,11):
                    print(count,end="")
                l = l - 10
            # when l <= 10, print for the rest of columns
            if (l > 0): 
                count = count+1
                for i in range(1,l+1):
                    print(count,end="")
                    
    # in hang don vi
    # print margins
    l = len(board)
    if (l > 9):
        print()
        print("  ",end="")
    else:
        print(" ", end="")
    # print numbers
    for i in range(1,l+1):
        print(i%10,end="")
    print()

def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """
    board_length = len(state)

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: '-'
    }

    if board_length < 10:
        row_index = 1
        # cho moi hang
        for row in state:
            print(row_index, end="")                # in so hang
            for cell in row:
                symbol = chars[cell]                # in o theo chars
                print(symbol, end='')
            print()
            # so hang tiep theo
            row_index+=1
    elif board_length >= 10:
        # in 10 hang dau tien, co thut dong
        for i in range(1, 10):
            print("", i, end="")                    # in so hang 
            for j in range(0, len(state[i - 1])):   # in noi dung hang i
                cell = state[i-1][j]
                symbol = chars[cell]
                print(symbol, sep="", end="")       # in symbol trong dict chars
            print()
        # in cac hang con lai tu 10 den 99
        for i in range(10,len(state)+1):
            print(i, end="")                        # in so hang tu 10
            for j in range(0, len(state[i-1])):     # in noi dung cua hang i
                cell = state[i-1][j]
                symbol = chars[cell]
                print(symbol,sep="",end="")         # in symbol theo dict chars
            print()


    
def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    initial_depth = depth
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render_column_indexes(board) # custom function
    render(board, c_choice, h_choice)

    if depth == len(board)*len(board): # depth = n mu 2
        x = choice(range(0,len(board)))  # choice = range from 0 to n
        y = choice(range(0,len(board)))
    else:
        alpha = [-1, -1, -infinity]
        beta = [-1, -1, +infinity]
        move = minimax(board, depth, COMP, initial_depth, alpha, beta)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def board_setup(c_choice, h_choice, player):
    choice = ''
    # game over check
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # display O and X
    clean()
    if player == COMP:
        choice = c_choice
    elif player == HUMAN:
        choice = h_choice
    
    print(f'Next: [{choice}]')
    render_column_indexes(board)    # custom function
    render(board, c_choice, h_choice)

    x = -1 
    y = -1
    while x < 0 or y < 0 or x >= len(board) or y >= len(board) :
        try:
            move = input('Use numpad (hang <khoang trang> cot): ')
            x, y = move.split()
            
            coord = [int(x)-1, int(y)-1]
            can_move = set_move(coord[0], coord[1], player)
            
            # to pass while check
            x = coord[0]
            y = coord[1]
            if not can_move:
                print('Nuoc di khong hop le, vui long nhap toa do o trong')
                x = -1 
                y = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Loi, vui long nhap theo dinh dang (x y)')
    
    # Check gameover again then Ask if player want to continue presetting
    if depth == 0 or game_over(board):
        return 'N'
    
    option = ' '
        
    while option != 'Y' and option != 'N':
        clean()
        render_column_indexes(board)
        render(board, c_choice, h_choice)
        try:
            option = input('Ban co muon nhap tiep [y/n]:' ).upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    return option
    
    
    
    

def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    """ For 3x3 only.
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }"""

    clean()
    print(f'Human turn [{h_choice}]')
    render_column_indexes(board)    # custom function
    render(board, c_choice, h_choice)

    x = -1 
    y = -1
    while x < 0 or y < 0 or x >= len(board) or y >= len(board) :
        try:
            move = input('Use numpad (hang <khoang trang> cot): ')
            x, y = move.split()
            
            coord = [int(x)-1, int(y)-1]
            can_move = set_move(coord[0], coord[1], HUMAN)
            
            # to pass while check
            x = coord[0]
            y = coord[1]
            if not can_move:
                print('Nuoc di khong hop le, vui long nhap toa do o trong')
                x = -1 
                y = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Loi, vui long nhap theo dinh dang (x y)')

# Tao board voi kich thuoc da nhap
def input_board_size():
    board_size = -1
    while board_size < 3 or board_size > 100:
            try:
                print('')
                board_size = int(input('Nhap kich thuoc ban co [3..100]: '))
                
                if (board_size < 3 or board_size > 100):
                    print('Vui long nhap tu 3 den 100') 
                
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Input khong hop le')
    board[:] = create_board(board_size)

def set_num_to_win():

    selection = ''
    while selection != 'Y' and selection != 'N':
        try:
            print('')
            selection = input('Ban muon thay doi so quan thang? [y/n] - Default: {} '.format(number_to_win)).upper()
            
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
             print('Input khong hop le')
    num = 0
    if selection == 'Y':
        while num < 3 or num > len(board):
                try:
                    print('')
                    num = int(input('Nhap so quan thang [3...{}]: '.format(len(board))))
                    
                    if (num < 3 or num > len(board)):
                        print('Vui long nhap tu 3 den {}'.format(len(board))) 
                    
                except (EOFError, KeyboardInterrupt):
                    print('Bye')
                    exit()
                except (KeyError, ValueError):
                    print('Input khong hop le')
        return num
    else:
        return 3
    

def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first
    board_preset = ''
    player = ''

    global board_size
    board_size = input_board_size()
    clean()
    
    global number_to_win
    number_to_win = 3               # default number to win
    if number_to_win < len(board):
        number_to_win = set_num_to_win()
    clean() 
    
    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Ban chon X hay O?\n>> ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    
    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'
    
    # Asking if want to setup the board (2P mode):
    clean()
    while board_preset != 'Y' and board_preset != 'N':
        try:
            board_preset = input('Ban co muon dat truoc quan? [y/n] ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
      
    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('Ban muon di truoc?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if first == 'Y':
        player = HUMAN
    else:
        player = COMP
        
    # Board setup
    if board_preset == 'Y':
        
        option = board_setup(c_choice, h_choice, player)
        while option == 'Y' and len(empty_cells(board)) > 0 and not game_over(board):
            player = player * -1
            option = board_setup(c_choice, h_choice, player)
        player = player * - 1 # Pass movement to the next player
    
    # First move after setting up
    if len(empty_cells(board)) > 0 and not game_over(board):
        if player == COMP:
            ai_turn(c_choice, h_choice)
        
    
    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        """        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''"""

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render_column_indexes(board)
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render_column_indexes(board)
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render_column_indexes(board)
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()

if __name__ == '__main__':
    main()
