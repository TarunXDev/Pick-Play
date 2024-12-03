import random
import time


usernames_list = []


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "tie"
    elif (user_choice == "rock" and opponent_choice == "scissors") or \
         (user_choice == "scissors" and opponent_choice == "paper") or \
         (user_choice == "paper" and opponent_choice == "rock"):
        return "user"  
    else:
        return "opponent"  


def display_result(user_choice, opponent_choice, result, opponent_name):
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"{opponent_name}'s choice: {opponent_choice.capitalize()}")
    if result == "tie":
        print("It's a tie! Well, that was a tough one!")
    elif result == "user":
        print("You win this round! 🎉")
    else:
        print(f"{opponent_name} wins this round! 😢")


def display_stats(user_score, opponent_score, total_rounds):
    print(f"\n----- Game Stats -----")
    print(f"Total rounds played: {total_rounds}")
    print(f"Your score: {user_score} | Opponent's score: {opponent_score}")
    if total_rounds > 0:
        win_percentage = (user_score / total_rounds) * 100
        print(f"Your win percentage: {win_percentage:.2f}%")
    print("-----------------------\n")


def save_highscore(username, highscore, user_score):
    if user_score > highscore:
        highscore = user_score
        print(f"Congratulations, {username}! You've set a new highscore: {highscore}!")
    else:
        print(f"Good job, {username}! Your highscore remains: {highscore}")
    return highscore


def random_event():
    events = [
        "Surprise! Double Points Round! 🏆",
        "Oops, the computer's feeling generous today! 🤗",
        "Watch out! The computer is on fire this round! 🔥",
        "Bonus Round! Guess what? You get an extra point for winning! 🎉"
    ]
    return random.choice(events)


def play_multiplayer():
    global usernames_list 

    print("Welcome to the Multiplayer Rock, Paper, Scissors Game! 🎮")

    
    while True:
        try:
            num_players = int(input("\nHow many players will play? (2 or more): "))
            if num_players >= 2:
                break
            else:
                print("You need at least 2 players to play. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    players = []
    
    for i in range(num_players):
        username = input(f"Enter username for Player {i+1}: ").strip()
        if username not in usernames_list:
            usernames_list.append(username)
        players.append(username)

    
    scores = {player: 0 for player in players}
    rounds_to_win = int(input("\nHow many rounds do you want to win to finish the game? (Choose 2, 4, 6, 10 etc.): "))
    total_rounds = 0

    print("\nAlright, let the multiplayer game begin! The first player to win the required rounds wins the game!")

    while all(score < rounds_to_win for score in scores.values()):
        print("\n----- Start a New Round -----")

       
        print(random_event())
        time.sleep(2)

        for i in range(num_players):
            user_choice = input(f"{players[i]}, Choose rock, paper, or scissors: ").lower()
            if user_choice not in ['rock', 'paper', 'scissors']:
                print("Oops! Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
                return

            
            opponent = players[(i + 1) % num_players]
            opponent_choice = input(f"{opponent}, Choose rock, paper, or scissors: ").lower()

           
            result = determine_winner(user_choice, opponent_choice)
            display_result(user_choice, opponent_choice, result, opponent)

            if result == "user":
                scores[players[i]] += 1
            elif result == "opponent":
                scores[opponent] += 1

            total_rounds += 1
            display_stats(scores[players[i]], scores[opponent], total_rounds)

        
        for player, score in scores.items():
            if score == rounds_to_win:
                print(f"\nCongratulations {player}, you won the game!")
                return

    
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nThanks for playing! See you next time! 🎉👋")
    else:
        play_multiplayer()  


def show_all_usernames():
    print("\nAll players who have played the game:")
    if usernames_list:
        for username in usernames_list:
            print(f"- {username}")
    else:
        print("No players have played yet.")
        

def play_computer():
    print("Welcome to the Rock, Paper, Scissors Game! 🎮")
    
    
    username = input("Enter your username: ").strip()
    
    
    if username not in usernames_list:
        usernames_list.append(username)

    print(f"\nUsernames that have played so far: {', '.join(usernames_list)}")

    
    highscore = 0
    
   
    win_goal = int(input("\nHow many rounds do you want to win to finish the game? (Choose 2, 4, 6, 10 etc.): "))
    
    user_score = 0
    computer_score = 0
    total_rounds = 0

    print(f"\nAlright, {username}! Let's start the game. First to {win_goal} wins!")

    time.sleep(2)
    
    while user_score < win_goal and computer_score < win_goal:
        print("\n----- Start a New Round -----")
        
       
        print(random_event())
        time.sleep(2)

        
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Oops! Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
            continue

        
        computer_choice = get_computer_choice()

       
        result = determine_winner(user_choice, computer_choice)

       
        display_result(user_choice, computer_choice, result, "Computer")

       
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        
        total_rounds += 1

       
        display_stats(user_score, computer_score, total_rounds)

    
    if user_score == win_goal:
        print(f"\nCongratulations {username}, you won the game with {user_score} wins!")
    else:
        print(f"\nSorry {username}, the computer won the game with {computer_score} wins!")

    
    highscore = save_highscore(username, highscore, user_score)

   
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nThanks for playing! See you next time! 🎉👋")
    else:
        play_computer()  


if __name__ == "__main__":
    while True:
        action = input("\nWould you like to play with the computer, multiplayer, or view all usernames? (computer/multiplayer/view): ").lower()
        if action == "computer":
            play_computer()
        elif action == "multiplayer":
            play_multiplayer()
        elif action == "view":
            show_all_usernames()
        else:
            print("Invalid option. Please choose again.")
