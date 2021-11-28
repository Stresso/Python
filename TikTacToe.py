board = []
global win
global full
win = False
full = False
global player


def spot():
    spot = False
    global board
    while not spot:
        global row
        global col
        row = int(input("Enter the row number:"))
        col = int(input("Enter the column number:"))
        print("\n")
        if row <= 3 and col <= 3:
            if board[row - 1][col - 1] == '-':
                board[row - 1][col - 1] = player
                spot = True
            else:
                print('Pick another spot')
        else:
            print('Invalid choice')


def create_board():
    print(f"Player {player}\n")
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    num = 0
    print(f"    1    2    3")
    for i in board:
        num += 1
        print(f'{num} {i}')


def check_win():
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == player:
                count += 1
        if count == 3:
            print(f'{player} Wins')
            exit()
    for i in range(3):
        count = 0
        for j in range(3):
            if board[j][i] == player:
                count += 1
        if count == 3:
            print(f'{player} Wins')
            exit()
    if True:
        count = 0
        for i in range(3):
            if board[i][i] == player:
                count += 1
        if count == 3:
            print(f'{player} Wins')
            exit()
        else:
            return
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f'{player} Wins')
        exit()
    else:
        return


def show_board():
    num = 0
    print(f"    1    2    3")
    for i in board:
        num += 1
        print(f'{num} {i}')
    check_win()
    check_full()


def player_swap():
    if player == 'X':
        return 'O'
    else:
        return 'X'


def check_full():
    for i in board:
        for j in i:
            if j == '-':
                return False
    print('Board is full hence Draw')
    exit()


player = 'X'
create_board()
while not win:
    spot()
    show_board()
    player = player_swap()


