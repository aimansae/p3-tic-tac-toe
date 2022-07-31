import random  # for computer as player

print('Welcome to the ultimate TIC TAC TOE Game!\n')
instructions = '''
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
            print(instructions)

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

player_symbol = 'x'


def game_board():
    
    '''
    Prints the game board '''
    while True:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        print(board[0], "| ", board[1], "| ", board[2], "| ",)
        print('-'*14)
        print(board[3], "| ", board[4], "| ", board[5], "| ",)
        print('-'*14)
        print(board[6], "| ", board[7], "| ", board[8], "| ",)
        print('\n')
        while True:
            try:

    
                user_input = int(input('Select a spot 1 to 9!:\n'))
        
                if user_input in range(1,10):
                    if board[user_input] == ' ':
                        board[user_input] = player_symbol
                        break
                    else:
                        print('The spot is taken')
                else:
                    print('Invalid selection. Number must be between 1/9')
            except ValueError:
                print("Please enter a valid number")

game_board()