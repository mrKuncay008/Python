
import os

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def draw_board():
    os.system('cls')
    print("\n\nTic Tac Toe\n\n")
    print("Aisma (X)  -  Poni (O)\n\n")
    print("     |     |     ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("     |     |     ")

def check_win():
    if board[1] == board[2] and board[2] == board[3]:
        return 1
    elif board[4] == board[5] and board[5] == board[6]:
        return 1
    elif board[7] == board[8] and board[8] == board[9]:
        return 1
    elif board[1] == board[4] and board[4] == board[7]:
        return 1
    elif board[2] == board[5] and board[5] == board[8]:
        return 1
    elif board[3] == board[6] and board[6] == board[9]:
        return 1
    elif board[1] == board[5] and board[5] == board[9]:
        return 1
    elif board[3] == board[5] and board[5] == board[7]:
        return 1
    elif board[1] != '1' and board[2] != '2' and board[3] != '3' and \
        board[4] != '4' and board[5] != '5' and board[6] != '6' and \
        board[7] != '7' and board[8] != '8' and board[9] != '9':
        return 0
    else:
        return -1

def main():
    player = 1
    draw_board()
    while True:
        if player % 2 != 0:
            player_choice = 'X'
        else:
            player_choice = 'O'

        print(f"Player {player}, enter a number: ")
        choice = int(input())
        if board[choice] == str(choice):
            board[choice] = player_choice
            player += 1
            draw_board()

        result = check_win()
        if result == 1:
            print(f"Player {player-1} wins!")
            break
        elif result == 0:
            print("Game draw!")
            break

if __name__ == "__main__":
    main()