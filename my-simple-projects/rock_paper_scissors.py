"""
Rock, Paper, Scissors game using the random module.
"""
import random

OPTIONS = ("rock", "paper", "scissors")


def get_computer_choice():
    """Pick a random choice for the computer."""
    return random.choice(OPTIONS)


def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        choice = input("Enter your choice (rock / paper / scissors): ").strip().lower()
        if choice in OPTIONS:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")


def decide_winner(user_choice, computer_choice):
    """
    Compare choices and return the result.
    Returns: "user", "computer", or "tie"
    """
    if user_choice == computer_choice:
        return "tie"
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    if wins[user_choice] == computer_choice:
        return "user"
    return "computer"


def play_round():
    """Play one round and return the result."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = decide_winner(user_choice, computer_choice)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

    return result


def main():
    print("=== Rock, Paper, Scissors ===\n")
    user_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        result = play_round()
        if result == "user":
            user_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            ties += 1

        print(f"\nScore — You: {user_wins}  Computer: {computer_wins}  Ties: {ties}")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y" and again != "yes":
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
