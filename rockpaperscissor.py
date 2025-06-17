import random 

def display_rules():
    print("\n----Game Rules----")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")

def determine_winner(user,computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
         return "user"
    else:
        return "computer"     

def rock_paper_scissor():
    choices = ["Rock","Paper","Scissor"]    


    while True:
        user_score = 0
        computer_score = 0
        round_number = 1


        print("---Welcome to Rock paper and scissor game---")
        print("Type 'rules' to see how to play, or type 'quit' to end the game...\n")

        while True:
            print(f"----Round Number {round_number}----")
            print("Available choices: ('rock','paper','scissor') ")
            user_choice = input("Enter your choice: ").lower()

            if user_choice == 'quit':
                print("Thanks for playing with us.")
                print(f"Final score => {user_score} | computer => {computer_score}\n")
                break
            elif user_choice == 'rules':
                display_rules()
                continue
            elif user_choice not in choices:
                print("Invalid input..Please input from above choices")
                continue

            computer_choice = random.choice(choices)
            print(f"computer choose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)

            if result == "tie":
                print("It's a tie")
            elif result == "user":
                print("You win this round")
                user_score += 1
            else:
                print("Computer wins")   
                computer_score += 1
            print(f"Final score => {user_score} | computer => {computer_score}\n")
            round_number += 1

        play_again = input("Would you like to play again ? (yes or no): ")
        if play_again != 'yes':
            print("Goodbye..")

if __name__ == "__main__":
    rock_paper_scissor()  


         






