import random as rd

def genpass(letters,n):
    password = ""
    i=0
    while i<n:
        x = rd.choice(letters)
        password += x
        i +=1
    return password


print("                                 ⚡⚡⚡Welcome to Random Password Generator by Mukal⚡⚡⚡")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_{}[()],.-+*&^%$#@!" ## valid entries for password(Should be changed if site doesnt support charcters)
while True:
    ask = input("Enter any key to gen pass or n to quit: ")    
    if(ask.lower() == 'n'):
        print("Thanks for using this program ❤️ .")
        break
    else:
        try:
            n  = int(input("Enter the number of letters needed for password: "))
            if(n < 0): # Checks if number entered is positive and not 0
                raise ValueError
            print(f"Your generated password is: {genpass(letters,n)}")
        except ValueError:
            print("Enter a positive number!")
            continue

