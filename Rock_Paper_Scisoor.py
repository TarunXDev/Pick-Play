import random
import time

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    if result == "tie":
        print("It's a tie! Well, that was a tough one!")
    elif result == "user":
        print("You win! Congratulations, you're a champion!")
    else:
        print("You lose! Better luck next time!")

# Function to display the stats
def display_stats(user_score, computer_score, total_rounds):
    print(f"\n----- Game Stats -----")
    print(f"Total rounds played: {total_rounds}")
    print(f"Your score: {user_score} | Computer's score: {computer_score}")
    if total_rounds > 0:
        win_percentage = (user_score / total_rounds) * 100
        print(f"Your win percentage: {win_percentage:.2f}%")
    print("-----------------------\n")

# Function to introduce fun random events
def random_event():
    events = [
        "Surprise! Double Points Round! 🏆",
        "Oops, the computer's feeling generous today! 🤗",
        "Watch out! The computer is on fire this round! 🔥",
        "Bonus Round! Guess what? You get an extra point for winning! 🎉"
    ]
    return random.choice(events)

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    total_rounds = 0

    print("Welcome to the Rock, Paper, Scissors Game! 🎮")
    print("Get ready for a fun challenge!")
    time.sleep(1)
    print("\nInstructions: Type 'rock', 'paper', or 'scissors' to play.")
    print("The computer will randomly choose, and we'll determine the winner together!")
    
    time.sleep(2)
    
    while True:
        print("\n----- Start a New Round -----")
        
        # Random events to make the game playful
        print(random_event())
        time.sleep(2)

        # Get user choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Oops! Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Display the result
        display_result(user_choice, computer_choice, result)

        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        # Update total rounds
        total_rounds += 1

        # Display stats
        display_stats(user_score, computer_score, total_rounds)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! See you next time! 🎉👋")
            break

# Run the game
if __name__ == "__main__":
    play_game()
