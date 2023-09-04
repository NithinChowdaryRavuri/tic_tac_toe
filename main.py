def display_board(board):
    print("  " + board[1] + "|" + board[2] + "|" + board[3])
    print("  -----")
    print("  " + board[4] + "|" + board[5] + "|" + board[6])
    print("  -----")
    print("  " + board[7] + "|" + board[8] + "|" + board[9])


def value_checker():
    choice = "x"
    while choice not in ["yes", "no"]:
        choice = input("Do you want to start the game (yes/no): ").lower()
        if choice not in ["yes", "no"]:
            print("Sorry! wrong selection. Please choose again: ")
    if choice == "no":
        return False
    if choice == "yes":
        return True


def player_mark():
    mark = "z"
    while mark not in ['x', 'o']:
        mark = input("Player-1: Choose your mark (x/o): ").lower()
        if mark not in ['x', 'o']:
            print("Sorry! wrong selection. Please choose again")
    if mark == 'x':
        return ['#', 'x', 'o']
    else:
        return ['#', 'o', 'x']


def space_validator(board, position):
    return board[position] == " "


def player_choice(board, num):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_validator(board, position):
        position = int(input("Player-" + str(num) + " Enter your choice location (1-9): "))
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_validator(board, position):
            print("Sorry! wrong selection. Please choose again")
    return position


def player_marker(board, marker, position):
    board[position] = marker


def win_check():
    if board[1] == board[2] == board[3] in ['x', 'o'] or board[4] == board[5] == board[6] in ['x', 'o'] or board[7] == \
            board[8] == board[9] in ['x', 'o'] or \
            board[1] == board[4] == board[7] in ['x', 'o'] or board[2] == board[5] == board[8] in ['x', 'o'] or \
            board[3] == board[6] == board[9] in ['x', 'o'] or \
            board[1] == board[5] == board[9] in ['x', 'o'] or board[7] == board[5] == board[3] in ['x', 'o']:
        return True


def full_check():
    for i in range(0, 10):
        if space_validator(board, i):
            return False
    return True


players_mark = []
position = 0

while True:
    if value_checker():
        board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        players_mark = player_mark()
        display_board(board)
        while True:
            position = player_choice(board, 1)
            player_marker(board, players_mark[1], position)
            if win_check():
                display_board(board)
                print("Congrats player-1")
                break
            if full_check():
                display_board(board)
                print("the game is a draw")
                break
            display_board(board)
            position = player_choice(board, 2)
            player_marker(board, players_mark[2], position)
            if win_check():
                display_board(board)
                print("Congrats player-2")
                break
            if full_check():
                display_board(board)
                print("the game is a draw")
                break
            display_board(board)
    else:
        print("Aarigatho! Hasthala vistha Baby :)")
        break
