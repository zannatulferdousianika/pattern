import random


print("Welcome to Guess number game")
print("You have 5 attempts per round")
print("You have to guess the number between 1 to 10")
print("Type 'quit' to end the game")

score = 0


while True:
  secretNumber = random.randint(1,10)
  attempts = 0
  maxAttempts = 5

  while attempts < maxAttempts:
    userInput = input(f"Enter your guess on attempts {attempts + 1} out of {maxAttempts}: ")
    if userInput.lower == 'quit':
        print("You have choosen to end the game...")
        print(f"Your score is: {score}")
        break
    try:
        guess= int(userInput)
    except ValueError:
        print("Invalid input...Please enter number between 1 to 10")
        continue

    if guess < 1 or guess >10:
        print("Your guess must be between 1 to 10")
        continue
    attempts += 1
    if guess < secretNumber:
        print("LOW.Guess again") 
        score -= 5
        print(f"Your current score: {score}") 
        continue  
    elif guess > secretNumber:
        print("TOO HIGH.Guess again") 
        score -= 5
        print(f"Your current score: {score}") 
        continue    
    else:
        print("Congratulations..You have guessed correct")
        score += 10
        print(f"Your current score: {score}")
        break
  else:
    print("GAME OVER.You have used all attempts.") 
    print(f"The correct number was: {secretNumber}") 
    print(f"Your final score is: {score}")
    break   
  
