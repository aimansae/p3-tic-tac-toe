'''while True:
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


        def check_column(board):
            '''
            Checks possible horizontal winning options
            '''
            pc_moves()
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
            global player_move
            if player_move == 'X':
                player_move = 'O'
            else:
                player_move = 'X'

        def pc_moves():
            ''' 
            Selects computer move randomly, based on player's move
            '''
            while player_move == 'O':
                computer_move = random.randint(1, 9)
                if board[computer_move] == ' ':
                    board[computer_move] = 'O'
                    change_player()


game_board()
