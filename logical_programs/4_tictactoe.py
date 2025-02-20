import random
print('Welcome to Tic Tac Toe\n')
board = [' ']*10
computer = 'O'
human = 'X'

def display_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}\n')

def check_win():
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    if board[1] == board[5] == board[9] != ' ':
        return True
    if board[3] == board[5] == board[7] != ' ':
        return True

    return False

def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False   
    
def is_available(position):
    return True if board[position] == ' ' else False

def insert(letter,position):
    if is_available(position):
        board[position] = letter
        display_board(board)
        if check_win():
            if letter == 'O':
                print("Computer Wins")
                exit()
            else:
                print("Human wins")
                exit()
        if check_draw():
            print("Draw")
            exit()
    else:
        if letter == 'X':
            position = int(input("Not Free! Please re-enter a position: "))
        else:
            position = random.randint(1, 9)
        insert(letter, position)

def human_move(human):
    position = int(input('Enter position to insert: '))
    insert(human,position)

def computer_move(computer):
    position = random.randint(1,9)
    insert(computer,position)
    
while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)
    