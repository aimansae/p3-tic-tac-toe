import random  # for computer as player

# main variables

player_symbol = 'X'

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = ''
computer = None

print('Welcome to the ultimate TIC TAC TOE Game!\n')
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


def game_board():
    '''
    Prints the game board 
    '''
    while True:
        print(board[1], "| ", board[2], "| ", board[3], "| ",)
        print('-'*14)
        print(board[4], "| ", board[5], "| ", board[6], "| ",)
        print('-'*14)
        print(board[7], "| ", board[8], "| ", board[9], "| ",)
        print('\n')
        while True:
            try:

                user_input = int(input('Select a spot 1 to 9!:\n'))

                if user_input in range(1, 10):
                    if board[user_input] == ' ':
                        board[user_input] = player_symbol
                        break
                    else:
                        print(
                            f'The spot {user_input} is taken. Choose a different number.')
                else:
                    print('Invalid selection. Number must be between 1/9')
            except ValueError:
                print("Please enter a valid number")

    def check_column(board):
        '''
        Checks possible horizontal winning options
        '''

        global winner
        if board[0] == board[1] == board[2] and board[1] != ' ':
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != ' ':
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != ' ':
            winner = board[6]
            return True

    check_column(board)

    def check_row(board):
        '''
        Checks possible vertically winning options
        '''
        global winner
        if board[0] == board[3] == board[6] and board[0] != ' ':
            winner = board[0]
            return True

        elif board[1] == board[4] == board[7] and board[1] != ' ':
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != ' ':
            winner = board[2]
            return True

    check_row(board)

    def check_oblique(board):
        '''
        Checks possible diagonally winning options
        '''
        global winner
        if board[0] == board[4] == board[8] and board[0] != ' ':
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != ' ':
            winner = board[2]
            return True

    check_oblique(board)

    def check_tie(board):
        '''
        Checks if there is no winner and it's a tie!
        '''
        if ' ' not in board:
            print("It's a tie!")
            game_board = False

    check_tie(board)

    def check_winner(board):
        ''' 
        Checks winner

        '''
        if check_row(board) or check_oblique(board) or check_column(board):
            print(f'The winner is {winner}!')

    check_winner(board)

    def change_player():
        ''' 
        Changes player 
        '''
        global player_symbol
        if player_symbol == 'X':
            player_symbol = 'O'
        else:
            player_symbol = 'X'

    def pc_moves():
        ''' 
        Selects computer move randomly, based on player's move
        '''
        while player_symbol == 'O':
            computer_move = random.randint(1, 9)
            if board[computer_move] == ' ':
                board[computer_move] = 'O'
                change_player()


game_board()
