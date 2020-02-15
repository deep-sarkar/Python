import random
class TicTacToe:

#TIC-TAC-TOE GAME
    #Create board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    def print_board(cls):
        for row in cls.board:
            print(row)

    #Play user
    def user_input(cls):
        print('user\'s turn...')
        __row = int(input('row : '))
        __column = int(input('Column : '))
        if cls.board[__row][__column] == " ":
            cls.board[__row][__column] = "X"
        else :
            print('user!! position already filled')
            cls.user_input()
   
    #Play computer
    def computer_input(cls):
        print('computer\'s turn...')
        __row = random.randrange(0,3)
        __column = random.randrange(0,3)
        if cls.board[__row][__column] == " ":
            cls.board[__row][__column] = "O"
        else :
            print('computer!! Position already filled')
            cls.computer_input()
    
    #Check win condition for user
    def check_win_user(cls):
        primary_doiagonal = 0
        secondary_diaggonal = 0
        for i in range(3):
            row = 0
            column = 0
            for j in range(3):
                if cls.board[i][j] == "X" : #Row win condition
                    row += 1
                if cls.board[j][i] == "X" : #column win condition
                    column += 1
                if i == j and cls.board[i][j] == "X" : #Primary diagonal win condition
                    primary_doiagonal += 1
                if i+j == 2 and cls.board[i][j] == "X" : #secondary diagonal win condition
                    secondary_diaggonal += 1
            if row == 3 or column == 3:
                return 1
                
        if secondary_diaggonal == 3 or primary_doiagonal == 3 :
            return 1

    #Check win condition for computer
    def check_win_computer(cls):
        primary_doiagonal = 0
        secondary_diaggonal = 0
        for i in range(3):
            row = 0
            column = 0
            for j in range(3):
                if cls.board[i][j] == "O" : #Row win condition
                    row += 1
                if cls.board[j][i] == "O" : #column win condition
                    column += 1
                if i == j and cls.board[i][j] == "O" : #Primary diagonal win condition
                    primary_doiagonal += 1
                if i+j == 2 and cls.board[i][j] == "O" : #secondary diagonal win condition
                    secondary_diaggonal += 1
            if row == 3 or column == 3:
                return 1
        if secondary_diaggonal == 3 or primary_doiagonal == 3 :
            return 1

tictack = TicTacToe()
tictack.print_board()
n = 9
while n > 0 :
    
    if n != 0:
        tictack.user_input()
        n -= 1
        tictack.print_board()
        ret = tictack.check_win_user()
        if ret == 1 :
            print('You won...')
            break
    if n != 0:
        tictack.computer_input()
        n -= 1
        tictack.print_board()
        ret = tictack.check_win_computer()
        if ret == 1 :
            print('computer won...')
            break

    