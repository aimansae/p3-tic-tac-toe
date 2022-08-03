import random  # for computer as player

# main variables for board, player's move, winner and computer's move

player_move = 'X'
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = None
computer = None
name = None

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
        global name
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
    asks the user to enter 'S' to in order to start the game
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
    print('-'*15)
    print(board[4], "| ", board[5], "| ", board[6], "| ",)
    print('-'*15)
    print(board[7], "| ", board[8], "| ", board[9], "| ",)
    print('\n')

# checking possible winning options


def check_rows(board):
    '''
    Checks possible horizontal winning options
    '''
    # accessing winner variable within the function
    global winner
    if board[1] == board[2] == board[3] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        winner = board[4]
        return True
    elif board[7] == board[8] == board[9] and board[9] != ' ':
        winner = board[7]
        return True


# check_rows(board)  # need to call this later in the actual game user choice!


def check_colum(board):
    '''
    Checks possible vertical winning options
    '''
    # accessing winner variable within the function
    global winner
    if board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[8] != ' ':
        winner = board[2]
        return True
    elif board[3] == board[6] == board[9] and board[9] != ' ':
        winner = board[3]
        return True


# check_colum(board)  # need to call this later in the actual game user choice!


def check_oblique(board):
    '''
    Checks possible oblique winning options
    '''

    global winner
    if board[1] == board[5] == board[9] and board[9] != ' ':
        winner = board[1]
        return True
    elif board[3] == board[5] == board[7] and board[7] != ' ':
        winner = board[3]
        return True


# check_oblique(board)  # need to call this later in the actual game user choice!


def check_tie(board):
    ''' 
    Check it there is no winner, prints a message stating it's a Tie.
    '''
    if ' ' not in board:
        print("It's a Tie!")


# need to stop the game and click return to the menu!


# check_tie(board)  # need to call this later in the actual game user choice!

# changing the player from player 'X' to computer 'O'


def change_player():
    ''' 
    Switches the player, accessing winner variable within the function with global
    '''
    global player_move
    if player_move == 'X':
        player_move = 'O'

    else:
        player_move = 'X'


# change_player() # need to call this later in the actual game user choice!


def computer_move(board):
    ''' 
    Chooses a random computer move after the player
    '''
    while player_move == 'O':
        pc_move = random.randint(1, 9)
        if board[pc_move] == ' ':
            board[pc_move] = 'O'
            change_player()


def who_is_the_winner():
    ''' 
    Check the winner evaluating the possible winning options defined above
    '''
    if check_rows(board) or check_oblique(board) or check_colum(board):
        print(f'The Winner is {winner}')
        return_to_first_page()


# need to stop the game and click return to the menu!


# who_is_the_winner() # need to call this later in the actual game user choice!

# clear the board if user want to play again

def reset_board():
    ''' 
    Clears the board in case user wants to play again
    '''
    board.clear()
    board.extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])


def return_to_first_page():
    ''' 
    Asks the user if they want to play again or quit when the game ends
    '''
    print('Game Ended!/n')

    print("Enter '1' to play again")
    print('Enter "Q" if you want to quit the game')
    while True:
        global name
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            print(f' Thank for playing the game {name}.')
            quit()
        elif make_a_choice == '1':
            print(f'Welcome again {name}')
            start_game()
            reset_board()
            user_choice()

        else:
            print("Invalid selection. Please select '1' or 'q'")


# actual game


def user_choice():
    '''
    checks users choice on board
    '''
    while True:
        game_board(board)

        while True:

            try:
                print("It's your turn!\n")
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

        who_is_the_winner()
        check_tie(board)
        change_player()
        computer_move(board)
        who_is_the_winner()
        check_tie(board)


user_choice()
