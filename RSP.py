import random
emojis = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    print(CYAN + "🎮 Welcome to Rock-Paper-Scissors!" + RESET)
    print(YELLOW + "Type 'quit' anytime to exit.\n" + RESET)

    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(MAGENTA + f"\n--- Round {round_number} ---" + RESET)
        user = input("Enter rock, paper, or scissors: ").strip().lower()
        if user == 'scissor':
            user = 'scissors'
        elif user == 'papers':
            user = 'paper'
        elif user == 'rocks':
            user = 'rock'

        if user == 'quit':
            print(CYAN + "\n🏁 Game Over! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! 👋" + RESET)
            break

        if user not in emojis:
            print(RED + "⚠️ Invalid input. Try again!" + RESET)
            continue

        computer = get_computer_choice()

        print(f"You chose: {user.capitalize()} {emojis[user]}")
        print(f"Computer chose: {computer.capitalize()} {emojis[computer]}")

        winner = determine_winner(user, computer)

        if winner == "tie":
            print(YELLOW + "🤝 It's a tie!" + RESET)
        elif winner == "user":
            user_score += 1
            print(GREEN + "🎉 You win this round!" + RESET)
        else:
            computer_score += 1
            print(RED + "💻 Computer wins this round!" + RESET)

        round_number += 1
play_game()
