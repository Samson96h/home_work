import random

def computer(last_digit, list):
    for _ in range(1000):
        num = str(random.randint(100, 999))
        if (last_digit == '0' or num[0] == last_digit) and num not in list:
            return num

def player_input():
    return input("Player 1, your turn: ")

def my_game():
    now = input("Player 1 enter a three-digit number: ")
    while not now.isdigit() or len(now) != 3:
        now = input("No! Enter a valid three-digit number: ")

    ml = [now]
    md = {'p1': 5, 'p2': 5}
    player = 2

    while md['p1'] > 0 and md['p2'] > 0:
        if player == 1:
            next_num = player_input()
            if next_num.lower() == "stop":
                print("Game stopped!")
                break
        else:
            print("Computer's turn...")
            next_num = computer(now[-1], ml)
            print(f"Computer chose: {next_num}")

        if not next_num.isdigit() or len(next_num) != 3:
            print("Invalid number!")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        if next_num in ml:
            print("This number has already been used!")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        if now[-1] == '0':
            print("Enter any number !")
        elif now[-1] != '0' and next_num[0] != now[-1]:
            print(f"No! The number must start with '{now[-1]}'")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        print("Correct!")
        ml.append(next_num)
        now = next_num
        player = 1 if player == 2 else 2

    if md['p1'] == 0:
        print("Player 1 — you lose!")
    elif md['p2'] == 0:
        print("Computer loses!")

    again = input("Play again? (yes/no): ").lower()
    if again == "yes":
        my_game()

my_game()
