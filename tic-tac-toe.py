turns = 0


def start():
    print("Welcome to the game of Tic-Tac-Toe! Player vs Player!")
    while True:
        begin_choice = input("Are you ready to begin? (Y/N): ").upper()
        if begin_choice == "Y":
            player1_choice = input("Player 1 (X or O): ").upper()
            if player1_choice == "X" or player1_choice == "O":
                game(player1_choice)
                break
        if begin_choice == "N":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter again.")


def game(p1):
    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"

    board_dict = {1: " ", 2: " ", 3: " ",
                  4: " ", 5: " ", 6: " ",
                  7: " ", 8: " ", 9: " "}
    global turns

    print("Player 1 has chosen to be {}, and Player 2 has chosen to be {}".format(p1, p2))
    print("Instruction: Choose a number between 1-9 (NumPad layout) to place your chosen character.")
    current_player = p1
    while True:
        print_board(board_dict)
        try:
            print(current_player + "'s turn.")
            player_move = int(input("Position: "))
        except ValueError:
            print("Input must be a number. Please try again.")
            continue
        if player_move < 1 or player_move > 9:
            print("The position number cannot be less than 1 or greater than 9. Please try again.")
            continue
        if board_dict[player_move] != " ":
            print("Position already taken. Please choose an another one.")
            continue

        board_dict[player_move] = current_player
        turns += 1

        if board_dict[7] == board_dict[8] == board_dict[9] == current_player:  # win position 7, 4, 9
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[4] == board_dict[5] == board_dict[6] == current_player:  # win position 4, 5, 6
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[1] == board_dict[2] == board_dict[3] == current_player:  # win position 1, 2, 3
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[1] == board_dict[4] == board_dict[7] == current_player:  # win position 1, 4, 7
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[2] == board_dict[5] == board_dict[8] == current_player:  # win position 2, 5, 8
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[3] == board_dict[6] == board_dict[9] == current_player:  # win position 3, 6, 9
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[1] == board_dict[5] == board_dict[9] == current_player:  # win position 1, 5, 9
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if board_dict[7] == board_dict[5] == board_dict[3] == current_player:  # win position 3, 6, 9
            print_board(board_dict)
            print(current_player, "is the winner!")
            break
        if turns == 9:
            print_board(board_dict)
            print("Draw! Nobody wins.")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    while True:
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            print("\n")
            start()
        else:
            print("Goodbye!")
            break


def print_board(board):
    print("\n| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |\n")


if __name__ == '__main__':
    start()
