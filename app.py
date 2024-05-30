import random

# Define the valid choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

# Function to get the player's choice
def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

# Main game loop
def play_game():
    player_score = 0
    total_rounds = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = random.choice(choices)
        
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win!")
            player_score += 1
        elif result == "lose":
            print("You lose!")
        else:
            print("It's a tie!")
        
        total_rounds += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Game over! You won {player_score} out of {total_rounds} rounds.")

# Run the game
if __name__ == "__main__":
    play_game()
