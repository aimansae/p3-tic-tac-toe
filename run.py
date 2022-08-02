import random  # for computer as player

# main variables for board, player's move, winner and computer's move

player_move = 'X'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = ''
computer = None

# welcome the user

print('Welcome to the ultimate TIC TAC TOE Game!\n')

# print instructions to play the game

show_instructions = '''
Here are the instructions: \n
- The game presents a 3x3 grid
- You will start first with the symbol 'X'
- The computer will be shown as the opposite symbol 'O'
- Place your symbol replacing one of the 9 numbers displayed
- The first among the players who have 3 same symbol in line, horizontally, vertically or    in a row Wins
- If all the 9 spots are full and no one wins it's a tie!
'''


def player_name():
    '''
    Gets player's name accepting only alphabetical characters
    '''

    while True:
        name = input("Please Enter your name:").capitalize()

        if name.isalpha():
            print("\n")
            print(f'Hi {name} welcome to the game!')
            print(show_instructions)

            break

        else:
            print(
                f'{name} is Invalid username. Only name with letter accepted. Please try again')


player_name()


def start_game():
    '''
    asks the user to click start in order to start the game
    '''

    while True:

        start_game_input = input("Type 'S' to start the game:").lower()

        if start_game_input == 's':
            print('Game starting...\n')
            break
        else:
            print(f"{start_game_input} Incorrect Input. Enter:'s' to start.")


start_game()


def game_board(board):
    '''
    Prints the game board
    '''

    print(board[1], "| ", board[2], "| ", board[3], "| ",)
    print('-'*14)
    print(board[4], "| ", board[5], "| ", board[6], "| ",)
    print('-'*14)
    print(board[7], "| ", board[8], "| ", board[9], "| ",)
    print('\n')

# checking possible winning options


def check_rows(board):
    '''
    Checks possible horizontal winning options
    '''
    # accessing winner variable within the function
    global winner
    if board[0] == board[1] == board[2] and board[1] != ' ':
        winner = board[0]
        print('checkRow')
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        winner = board[4]
        print('2checkRow')
    elif board[6] == board[7] == board[8] and board[8] != ' ':
        winner = board[4]
        print('3checkRow')


check_rows(board)  # need to call this later in the actual game user choice!


def check_colum(board):
    '''
    Checks possible vertical winning options
    '''
    # accessing winner variable within the function
    global winner
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board[0]
        print('checkcol')
    elif board[1] == board[4] == board[7] and board[7] != ' ':
        winner = board[1]
        print('2checkRow')
    elif board[2] == board[5] == board[8] and board[8] != ' ':
        winner = board[2]
        print('3checkRow')


check_colum(board)  # need to call this later in the actual game user choice!


def check_oblique(board):
    '''
    Checks possible oblique winning options
    '''
    # accessing winner variable within the function
    global winner
    if board[0] == board[4] == board[8] and board[8] != ' ':
        winner = board[0]
        print('check diag')
    elif board[2] == board[4] == board[6] and board[6] != ' ':
        winner = board[2]
        print('check diag')


check_oblique(board)  # need to call this later in the actual game user choice!


def check_tie(board):
    if ' ' not in board:
        print("It's a Tie!")


check_tie(board)
# neet to stop the game and click return to the menu!

# actual game


def user_choice():
    '''
    checks users choice on board
    '''
    while True:
        game_board(board)

        while True:

            try:
                user_input = int(input('Select a spot 1 to 9!:\n'))

                if user_input in range(1, 10):
                    if board[user_input] == ' ':
                        board[user_input] = player_move
                        break
                    else:
                        print(
                            f'The spot {user_input} is taken. Choose a another number.')
                else:
                    print('Invalid selection. Number must be between 1/9')

            except ValueError:
                print("Please enter a valid number")


user_choice()
