import random as rd

class InvalidChoiceError(Exception):
    pass

points = 0
choices = ("Snake", "Water", "Gun")
print("     Welcome to Snake, Water, Gun")


def checkWin(num1 , num2):
    if(num1 == num2): #Draw Condition
        return 0
    elif(num1 - num2 == -1 or num1 - num2 == 2 ): #Win condition
        return 1
    else: #Lose mf
        return -1
    
while True:
    try:
        inputs = input("Enter choice:\n           Snake--->(1)\n           Water--->(2)\n           Gun----->(3)\n")
        choice = int(inputs) - 1
        if choice not in [0,1,2]:
            raise InvalidChoiceError
        
    except InvalidChoiceError:
        print("Enter a number 1,2 or 3!")
        continue

    except ValueError:
        print("Enter a number!")
        continue
    
    computer = rd.randrange(0, 3)
    result = checkWin(choice, computer)
    
    if(result == 0):
        print(f"You chose: {choices[choice]}")
        print(f"Computer chose: {choices[computer]}\n")
        print("    Draw\n")
        print(f"Current Points = {points}")

    if(result == 1):
        print(f"You chose: {choices[choice]}")
        print(f"Computer chose: {choices[computer]}\n")
        print("    Win!!\n")
        points += 10
        print(f"Current Points = {points}")
    

    if(result == -1):
        print(f"You chose: {choices[choice]}")
        print(f"Computer chose: {choices[computer]}\n")
        print("    You Lost :(\n")
        print(f"Highest Points = {points}")
        points = 0

    playagain = input("Press any key to play again or N to exit.\n")
    if(playagain.lower() == "n"):
        print("Thanks for Playing!")
        break
    
   