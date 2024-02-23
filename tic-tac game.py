import random

board = list(range(1, 10))
used_numbers = []

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def choice_player():
    x = int(input('Введите число, чтобы поставить крест: '))
    if x not in used_numbers:
        used_numbers.append(x)
        for i in range(len(board)):
            if x == board[i]:
                board[i] = 'X'
                return True
        return False

def choice_bot():
    print('Ход компьютера')

    num_bot = random.randint(1, 9)
    while num_bot in used_numbers:
        num_bot = random.randint(1, 9)

    used_numbers.append(num_bot)

    for i in range(len(board)):
        if num_bot == board[i]:
            board[i] = 'O'
            return True
    return False

def check_winner(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        if all(elem == 'X' or elem == 'O' for elem in board):
            return 'Ничья'
    return False

while True:
    draw_board(board)
    if choice_player():
        if check_winner(board) == 'X':
            print('You win')
            break
    draw_board(board)
    if choice_bot():
        if check_winner(board) == 'O':
            print('Computer wins')
            break
    if check_winner(board) == 'Ничья':
        print('Никто не выиграл')
        break