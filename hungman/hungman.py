from random import randint

stages = [
    """ 
     ------
     |    |
          |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
          |
    =========
    """
]

def get_word(file_name):
    try:
        with open(file_name) as f:
            words = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Word file not found. Using default word.")
        return "python"
    return words[randint(0, len(words) - 1)]

def play_game():
    wrong_guesses = 0
    secret_word = get_word('words.txt')
    guessed_word = ["-" for _ in secret_word]
    used_letters = []

    while "".join(guessed_word) != secret_word and wrong_guesses < 6:
        print("".join(guessed_word))
        print(stages[wrong_guesses])
        guess = input("Enter a letter: ").lower()

        if guess in used_letters:
            print("You already guessed that letter.")
            continue

        used_letters.append(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            wrong_guesses += 1

    if "".join(guessed_word) == secret_word:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(stages[-1])
        print(f"You lost. The word was: {secret_word}")

def main():
    play_game()

if __name__ == '__main__':
    main()