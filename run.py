print('Welcome to the ultimate TIC TAC TOE Grame!\n')


def player_name():
    '''
    Gets player's name accepting only alphabetical characters
    '''

    while True:
        name = input("Please Enter your name: ").lower()

        if name.isalpha():
            print(
                f'{name} Welcome to the game . \n Please Follow the instructions below: ')
            break

        else:
            print(
                f'{name} is Invalid username. Only name with letter accepted. Try again')


player_name()
