import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficalty. Type 'easy' or 'hard': ").lower()
sys_value = random.randint(1, 100)
print(sys_value)

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Please select correct level")

def guess_game():
    global attempts
    while attempts > 0:
        # attempts = attempts
        # print("True")
        print(f"You have {attempts} remaining to guess the number.")
        guess_value = int(input("Make a guess: "))
        attempts -= 1
        if guess_value > sys_value:
          print("Too high.\nGuess again.")
          # print(f"You have {attempts} remaining to guess the number.")
        elif guess_value < sys_value:
          print("Too low.\nGauess again.")
          # print(f"You have {attempts} remaining to guess the number.")
        elif guess_value == sys_value:
          print("Your guess is correct")
          attempts = 0
guess_game()
