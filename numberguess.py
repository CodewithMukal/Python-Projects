import random as rd

print("      WELCOME TO NUMBER GUESSING GAME BY CODEWITHMUKAL!")
print("Rules:\n1. If guess is within a limit of 10, you will be told you are close.\n2. If guess is more than 10 digits away you will be told your guess is too high or low.\n3. Each Guess will increase your attempts.\n")
print("Choose a range: (A,B)")
A = int(input("Enter the value of A: "))
print(f"The range is now: ({A},B)")
B = int(input("Enter the value of B: "))
print(f"\nThe range is now: ({A},{B}) with {A} and {B} included\n")

attempts = 0
print("The computer has selected a number from given range.")
print("Try to guess it in minimum number of attempts by 1.")
computer = rd.randint(A,B)
while True:
    guess = int(input("Enter your guess: "))
    if(guess == computer):
        print("Congratulations! You have guessed the number.")
        attempts += 1
        print(f"The number of guesses were : {attempts}")
        x = input("Enter any key to exit: ")
        if(x == "n"):
            break
        else:
            break        
    if(guess-computer > 10):
        print("Your guess is too high.")
        attempts += 1
        print(f"Attempts: {attempts}")
    elif(guess-computer <= 10 and guess-computer>0):
        print("Your guess is close but high.")
        attempts += 1
        print(f"Attempts: {attempts}")
    elif(guess-computer < -10):
        print("Your guess is too low.")
        attempts += 1
        print(f"Attempts: {attempts}")
    elif(guess-computer >= -10 and guess-computer<0):
        print("Your guess is close but low.")
        attempts += 1
        print(f"Attempts: {attempts}")