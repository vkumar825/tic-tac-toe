import random

def game(p1):
    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"

    board_pos = {1: " ", 2: " ", 3: " ",
                  4: " ", 5: " ", 6: " ",
                  7: " ", 8: " ", 9: " "}
    turns = 0
    print("\nInstruction: Choose a number between 1-9 (NumPad layout) to place your chosen character.")
    current_player = p1
    while True:
        # game_board(board_dict)
        try:
            turns += 1
            print("\n\t   Round", turns)
            game_board(board_pos)
            print(current_player + "'s turn.")
            player_move = int(input("Position: "))
        except ValueError:
            print("Input must be a number. Please try again.")
            continue
        if player_move < 1 or player_move > 9:
            print("The position number cannot be less than 1 or greater than 9. Please try again.")
            continue
        if board_pos[player_move] != " ":
            print("Position already taken. Please choose an another one.")
            continue

        board_pos[player_move] = current_player

        if board_check(board_pos, current_player):
            game_board(board_pos)
            print(current_player, "is the winner!")
            play_again(p1)
            break

        if turns == 9:
            game_board(board_pos)
            print("Draw! Nobody wins.")
            break

        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

def game_board(board):
    print("\n\t| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("\t| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("\t| " + board[1] + " | " + board[2] + " | " + board[3] + " |\n")

def board_check(board, current_player):
    if board[7] == board[8] == board[9] == current_player:  # win position 7, 8, 9
        return True
    if board[4] == board[5] == board[6] == current_player:  # win position 4, 5, 6
        return True
    if board[1] == board[2] == board[3] == current_player:  # win position 1, 2, 3
        return True
    if board[1] == board[4] == board[7] == current_player:  # win position 1, 4, 7
        return True
    if board[2] == board[5] == board[8] == current_player:  # win position 2, 5, 8
        return True
    if board[3] == board[6] == board[9] == current_player:  # win position 3, 6, 9
        return True
    if board[1] == board[5] == board[9] == current_player:  # win position 1, 5, 9
        return True
    if board[7] == board[5] == board[3] == current_player:  # win position 7, 5, 9
        return True

def play_again(p1):
    while True:
        play_again = input("Play again with same characters? (Y/N): ").upper()
        if play_again == "Y":
            game(p1)
        if play_again == "N":
            print("Goodbye!")
            break

if __name__ == '__main__':
    print("Welcome to the game of Tic-Tac-Toe! Player vs Player!")
    while True:
        begin_choice = input("Are you ready to begin? (Y/N): ").upper()
        if begin_choice == "Y":
            player1_choice = input("Player 1 (X or O): ").upper()
            if player1_choice == "X" or player1_choice == "O":
                game(player1_choice)
                break
        else:
            print("Goodbye!")
            break
        