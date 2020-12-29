"""
Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os/“X’y O’sies” (Ireland), is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. It is a solved game with a forced draw assuming best play from both players. (https://en.wikipedia.org/wiki/Tic-tac-toe)
"""
import os
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

def get_new_board():
    return [str(x) for x in range(1, 10)]

def board_rendered(board: list) -> str:
    res = ''
    rows = []
    for r in range(3):
        start = r * 3
        end = start + 3
        row = board[start:end]
        rows.append(' | '.join(row))
    return '\n---------\n'.join(rows)

def get_winning_slices():
    slices = []
    for r in range(3):
        start = r * 3
        end = start + 3
        row = slice(start, end, None)
        slices.append(row)
    
    for c in range(3):
        start = c
        end = 6 + c + 1
        col = slice(start, end, 3)
        slices.append(col)

    diag_1 = slice(0, 9, 4)
    diag_2 = slice(2, 7, 2)
    slices.append(diag_1)
    slices.append(diag_2)
    
    return slices

def check_win_slice(sl, board):
    return all(board[sl][0] == x for x in board[sl])

def is_winner(board):
    return any(check_win_slice(sl, board) for sl in get_winning_slices())


def player_gen(name_x='Player 1', name_o='Player 2'):
    players = [{'name': name_x, 'symb': 'X'},
               {'name': name_o, 'symb': 'O'}]
    i = 0
    while True:
        ind = i % 2
        yield players[ind]
        i += 1

def get_input(player, board):
    while True:
        inp = input(f"{pl['name']} type the position for {pl['symb']} : ")

        pos = None    
        if inp in ['q', 'n']:
            return inp
        
        try:
            pos = int(inp)
            pos -= 1
            if board[pos] in 'XO':
                print('This cell is busy.')
                print('Try one more time.')
                print()
                continue
            return pos
        except (ValueError, IndexError) as e:
            print('Wrong input. You should put the number 1-9.')
            print('Try one more time.')
            print()

def init_game(name_x='Player 1', name_o='Player 2'):
    board = get_new_board()
    player = player_gen(name_x, name_o)
    return board, player

menu_text = """
1 - 9 the number of a cell to put X or O
q - Terminate the current game & Exit
n - Terminate the current game & Start new game
"""

board, player = init_game()
while True:
    cls()
    print(board_rendered(board))
    print(menu_text)

    pl = next(player)
    inp = get_input(pl, board)

    if inp == 'q':
        print('='*30)
        print('Exit')
        print()
        break
    elif inp == 'n':
        print('='*30)
        print('Terminating the current game & starting new one')
        print()
        sleep(4)
        board, player = init_game()
        continue
    else:
        board[inp] = pl['symb']
        if is_winner(board):
            print(f"{pl['name']} is 'WINNER!!!!'")
            sleep(4)
            board, player = init_game()


