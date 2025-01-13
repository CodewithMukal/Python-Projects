import random as rd

print("                 WELCOME TO WORD GUESS GAME BY MUKAL\n")


def ent():    #Function to enter words in our list
    n = int(input("Enter the number of words you will enter: "))
    words = []
    i = 0
    while i < n:
        x = input(f"Enter word number {i+1}:")
        if(len(x) <= 1 or x in words): # if short word or repeated then renter the word boy!
            print("Enter word again!!!!")
            continue
        else:
            words.append(x)
            i+=1
    else:
        start(words) #Start the game when all words are entered
        
def win(player,comp,attempts): #check if player has won or not
    if(player == comp):
        attempts += 1
        print(f"Win! You guessed the number in {attempts} attempts.")
        attempts = 0
        replay =  input("Enter any key to continue or N to exit: ")
        if(replay.lower()=='n'): #exit the game upon enetring N or n
            print("Thanks for Playing!")
            exit()
        else:
            ent() #Restart the game
    else:
        return 0

def start(words):
    comp = rd.choice(words)
    attempts = 0
    print("Computer has chosen a words. Guess it in min number of attempts.")
    while True:
        player = input("Enter your guess: ")
        if(win(player,comp,attempts)==0): # Wrong guess and retry and atempts++
            attempts += 1
            print("Wrong Guess! Try Again")
            print(f"Attempts: {attempts}")
            continue
        else:
            win(player,comp,attempts) # Won the game,  exit or replay

ent() #starting the game