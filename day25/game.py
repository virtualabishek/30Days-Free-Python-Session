# Game
import random # random vane module import gareko.
# computer le S,R,P -> randomly order -
def get_choice_from_computer():
    randomNum = random.randint(1,3)
    options = {1: "rock", 2: "paper", 3: "scissors"}
    computerChoice = options[randomNum]
    return computerChoice
computerChoice = get_choice_from_computer()

def get_input_from_user():
    inputFromUser = input("Enter your choice. rock/scissors/paper: ")
    inputFromUser = inputFromUser.lower()
    return inputFromUser

inputFromUser = get_input_from_user()

def checkResult(computerChoice, inputFromUser):
    if computerChoice == inputFromUser:
        return "Draw"
        # User wins
    elif inputFromUser == "rock" and computerChoice == "scissors":
        return "Win"
    elif inputFromUser == "paper" and computerChoice == "rock":
        return "Win"
    elif inputFromUser == "scissors" and computerChoice == "paper":
        return "Win"
    else:
        return "Lose"



finalResult = checkResult(computerChoice, inputFromUser)

print(f"You picked: {inputFromUser}")
print(f"Computer Picked: {computerChoice}")
# print(f"Result is: {finalResult}")

if finalResult == "Win":
    print("User wins the game.")
elif finalResult == "Loose":
    print("Computer Wins the Game")
else:
    print("The game is draw.")
    

    

