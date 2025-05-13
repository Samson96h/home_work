def my_game ():
    now = input("Player 1 enter a three-digit number : ")
    while not now.isdigit() or len(now) != 3:
        now = input("Noo ! enter a three-digit number : ")

    ml = [now]
    md = {'p1': 5, 'p2': 5}
    player = 2

    while md['p1'] > 0 and md['p2'] > 0:
        next_num = input(f"Player {player}, your turn : ")

        if next_num.lower() == "stop":
            print("The game is stopped !")
            break

        if not next_num.isdigit() or len(next_num) != 3:
            print("You need to enter a three-digit number !")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        if next_num in ml:
            print("You can't repeat numbers !")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        if now[-1] == '0':
            print("Enter any number!")
        elif next_num[0] != now[-1]:
            print(f"No ! The number must start the with '{now[-1]}'")
            md[f'p{player}'] -= 1
            print(f"Player {player} has {md[f'p{player}']} lives left")
            continue

        print("Right!")
        ml.append(next_num)
        now = next_num
        player = 1 if player == 2 else 2

    if md['p1'] == 0:
        print("Player 1 - you lose!")
    elif md['p2'] == 0:
        print("Player 2 - you lose!")

    again = input("Play again? (yes/no): ").lower()
    if again == "yes":
        my_game()

my_game()