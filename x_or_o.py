ml = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def board(board_data):
    for row in board_data:
        print(" ".join(row))
    print()


def check_winner(board_data):
    for row in board_data:
        if row == ["x", "x", "x"]:
            return "X"
        elif row == ["o", "o", "o"]:
            return "O"

    for col in range(3):
        if board_data[0][col] == board_data[1][col] == board_data[2][col] != "-":
            return board_data[0][col].upper()

    if board_data[0][0] == board_data[1][1] == board_data[2][2] != "-":
        return board_data[0][0].upper()
    if board_data[0][2] == board_data[1][1] == board_data[2][0] != "-":
        return board_data[0][2].upper()

    for row in board_data:
        if "-" in row:
            return "D"
    return "T"


def game(board_data):
    player = 1
    while True:
        board(board_data)
        print(f"Player {player}, enter your move (row and column from 1 to 3): ")
        answ = input()
        parts = answ.split()

        if len(parts) != 2:
            print("Invalid input. You must enter two numbers.")
            continue

        if not (parts[0].isdigit() and parts[1].isdigit()):
            print("Please enter numbers only.")
            continue

        row = int(parts[0]) - 1
        col = int(parts[1]) - 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Numbers must be between 1 and 3.")
            continue

        if board_data[row][col] != '-':
            print("That cell is already taken. Try again.")
            continue

        if player == 1:
            board_data[row][col] = "x"
            player = 2
        else:
            board_data[row][col] = "o"
            player = 1

        result = check_winner(board_data)
        if result == "X":
            board(board_data)
            print("Player 1 (X) wins!")
            break
        elif result == "O":
            board(board_data)
            print("Player 2 (O) wins!")
            break
        elif result == "T":
            board(board_data)
            print("It's a tie!")
            break


def main():
    game(ml)


if __name__ == "__main__":
    main()
