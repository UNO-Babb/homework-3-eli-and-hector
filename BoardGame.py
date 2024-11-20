#Example Flask App for a hexaganal tile game
#Logic is in this python file

import random

def roll_dice():
    """Simulates rolling two dice and returns their sum and individual values."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2, die1 + die2

def dice_game():
    """Main function to play the dice game."""
    print("Welcome to the Dice Game!")

    # Get the number of players
    while True:
        try:
            num_players = int(input("Enter the number of players (2-5): "))
            if 2 <= num_players <= 5:
                break
            else:
                print("Please enter a number between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Initialize player list
    players = [f"Player {i + 1}" for i in range(num_players)]

    print("\nGame Start! First to roll a 7 or 11 wins. Roll 1 and 1 to lose.")
    print("Pass the dice for other rolls. Let's begin!\n")

    while True:
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            die1, die2, total = roll_dice()

            print(f"You rolled {die1} and {die2} (Total: {total})")

            if total == 7 or total == 11:
                print(f"\nCongratulations, {player}! You rolled a {total} and won the game!\n")
                return

            elif die1 == 1 and die2 == 1:
                print(f"\nOh no, {player}! You rolled a 1 and 1 and lost the game.\n")
                return

            else:
                print(f"{player} did not win or lose. Passing the dice to the next player.\n")

# Run the game
dice_game()

