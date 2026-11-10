"""
Mini Games Collection
A simple Python project with three classic games:
1. Number Guessing Game
2. Rock Paper Scissors
3. Hangman
"""

import random


def number_guessing():
    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return

    print(f"Out of attempts! The number was {number}.")


def rock_paper_scissors():
    print("\n--- Rock Paper Scissors (Best of 5) ---")
    choices = ["rock", "paper", "scissors"]
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    player_score = 0
    computer_score = 0

    for round_no in range(1, 6):
        player = input(f"Round {round_no} - rock, paper or scissors? ").strip().lower()
        if player not in choices:
            print("Invalid choice, you lose this round.")
            computer_score += 1
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif beats[player] == computer:
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

    if player_score > computer_score:
        print("You won the game! Congratulations!")
    elif player_score < computer_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game is a draw!")


def hangman():
    print("\n--- Hangman ---")
    words = ["python", "program", "keyboard", "internet", "developer",
             "function", "variable", "computer", "github", "project"]
    word = random.choice(words)
    guessed = set()
    lives = 6

    while lives > 0:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Lives left: {lives}")

        if "_" not in display:
            print("You won! The word was:", word)
            return

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        if guess in word:
            print("Good guess!")
        else:
            lives -= 1
            print("Wrong guess!")

    print(f"\nGame over! The word was: {word}")


def main():
    print("=" * 35)
    print("   WELCOME TO MINI GAMES COLLECTION")
    print("=" * 35)

    while True:
        print("\nChoose a game:")
        print("1. Number Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Hangman")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            number_guessing()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            hangman()
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
