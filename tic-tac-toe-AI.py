import random

def default():
    print("\nWelcome! Let's play TIC TAC TOE!\n")

def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board are the same as the right side of your keyboard.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position (1-9).")

def play():
    return input("\nAre you ready to play the game? Enter [Y]es or [N]o.\t").upper().startswith('Y')

def names():
    p1_name = input("\nEnter NAME of PLAYER 1:\t").capitalize()
    p2_name = "Computer"  # Fixed opponent name
    return p1_name, p2_name

def choice(p1_name):
    p1_choice = ' '
    while p1_choice not in ['X', 'O']:
        p1_choice = input(f"\n{p1_name}, Do you want to be X or O?\t")[0].upper()
        if p1_choice not in ['X', 'O']:
            print("INVALID INPUT! Please Try Again!")
    p2_choice = 'O' if p1_choice == 'X' else 'X'
    return p1_choice, p2_choice

def first_player():
    return random.choice((0, 1))

def display_board(board):
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))
    print("-----------")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("-----------")
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))

def player_choice(board, name, choice):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))
        if position not in range(1, 10) or not space_check(board, position):
            print("INVALID INPUT. Please Try Again!\n")
    return position

def computer_choice(board, choice):
    available_positions = [pos for pos in range(1, 10) if space_check(board, pos)]
    position = random.choice(available_positions)
    print(f"\nComputer chose position {position} ({choice})!")
    return position

def place_marker(board, choice, position):
    board[position] = choice

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(space != ' ' for space in board[1:])

def win_check(board, choice):
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    return any(all(board[pos] == choice for pos in combo) for combo in win_combinations)

def replay():
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')

def main():
    print("\n\t\t NAMASTE! \n")
    input("Press ENTER to start!")

    default()
    rules()

    while True:
        theBoard = [' '] * 10
        p1_name, p2_name = names()
        p1_choice, p2_choice = choice(p1_name)
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

        turn = p1_name if first_player() else p2_name
        print(f"\n{turn} will go first!")

        play_game = play()

        while play_game:
            display_board(theBoard)

            if turn == p1_name:
                position = player_choice(theBoard, p1_name, p1_choice)
                place_marker(theBoard, p1_choice, position)

                if win_check(theBoard, p1_choice):
                    display_board(theBoard)
                    print(f'\n\nCONGRATULATIONS {p1_name}! YOU HAVE WON THE GAME!\n\n')
                    play_game = False
                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print('\nThe game is a DRAW!\n')
                    break
                else:
                    turn = p2_name
            else:  # Computer's turn
                position = computer_choice(theBoard, p2_choice)
                place_marker(theBoard, p2_choice, position)

                if win_check(theBoard, p2_choice):
                    display_board(theBoard)
                    print(f'\n\nCONGRATULATIONS {p2_name}! YOU HAVE WON THE GAME!\n\n')
                    play_game = False
                elif full_board_check(theBoard):
                    display_board(theBoard)
                    print('\nThe game is a DRAW!\n')
                    break
                else:
                    turn = p1_name

        if not replay():
            break

    print("\n\n\t\t\tTHE END!")

if __name__ == "__main__":
    main()
