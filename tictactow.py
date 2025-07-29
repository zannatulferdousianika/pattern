import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*10)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][j] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != '' for row in board for cell in row)

def get_computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board,"O"):
                    board[i][j] = " "
                    return(i, j)
                board[i][j] = " "  
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board,"X"):
                    board[i][j] = " "
                    return(i, j)
                board[i][j] = " "           
    empty_cells = [(i,j) for i in range(3) for j in range(3)== " "]
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    print("Welcome to TIC TAC TOE")
    print("Enter 'q' at anytime to exit the game")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X","O"]
    current_player = 0

    while True:
        print_board(board)
        if current_player == 0:
            print(f"player{players[current_player]}'s turn")
            try:
                row_input = input("Enter row(1-3):")
                if row_input.lower() == 'q':
                    print("Game quit")
                    break

                col_input = input("Enter col(1-3):")
                if col_input.lower() == 'q':
                    print("Game quit")
                    break

                row ,col = int(row_input)- 1 , int(col_input)- 1
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input")
                    continue
                if board[row][col] != " ":
                    print("Cell is already taken")
                    continue
            except ValueError:
                print("Invalid input")
                continue
        else:
            print("Computer's turn'O': ")
            move = get_computer_move(board)
            if move:
                row,col = move
                print(f"Computer chooses row{row+1} and coloum{col+1}")
            else:
                print("No moves left for computer")   
                break

        board[row][col] = players[current_player] 

        if check_winner(board, players[current_player]):
            print_board(board)
            if current_player == 0:
                print(f"player {players[current_player]} wins")
            else:
                print("Computer 'O' wins") 
            break

        if is_full(board):
            print_board(board)   
            print("It's a draw!")
            break
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()

    






       