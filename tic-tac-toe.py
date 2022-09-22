'''
Tic-Tac-Toe
Author: Logan Bugg
'''

def main():
    # make board, x goes first
    player = "x"
    board = make_board()

    # loop to play game until finished
    while not (game_draw(board) or game_win(board)):
        show_board(board)
        play_turn(player, board)
        player = change_players(player)
    
    # show board at end and print finished message
    show_board(board)
    print("Good game. Thanks for playing!")

# create array with numbers 1-9
def make_board():
    board = []
    for num in range(9):
        board.append(num + 1)
    return board

# replace array value with x or o
def play_turn(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

# switch player from x to o, or vice versa
def change_players(current):
    if current == "o":
        return "x"
    else:
        return "o"

# display current state of board
def show_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}\n")

# any row of 3 of the same is a win
def game_win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[6] == board[4] == board[2])

# if every spot is now a letter, and the game isn't won, end in a draw
def game_draw(board):
    for num in range(9):
        if board[num] != "x" and board[num] != "o":
            return False
        else:
            return True

if __name__ == "__main__":
    main()