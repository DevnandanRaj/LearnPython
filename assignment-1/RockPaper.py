import random

def getUsersChoice():
    while True:
        userChoice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if userChoice in ["rock", "paper", "scissors"]:
            return userChoice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def getComputerChoice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif (
        (userChoice == "rock" and computerChoice == "scissors")
        or (userChoice == "paper" and computerChoice == "rock")
        or (userChoice == "scissors" and computerChoice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        userChoice = getUsersChoice()
        computerChoice = getComputerChoice()

        print(f"You chose {userChoice}.")
        print(f"The computer chose {computerChoice}.")

        result = determine_winner(userChoice, computerChoice)
        print(result)

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break

    print("Thanks for playing!")
if __name__ == "__main__":
    main()