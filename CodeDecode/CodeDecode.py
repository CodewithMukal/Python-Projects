import random
import string

rndm = ''.join(random.choices(string.ascii_letters, k=2))
rndm2 = ''.join(random.choices(string.ascii_letters, k=2))

def code(word):
    if(len(word) <=2):
        return word[::-1]
         
    else:
       word += word[0]
       word = word[1:]
       word = rndm+word+rndm2
       return word
    
def decode(word):
   if(len(word) <=2):
      return word[::-1]
   else:
      word = word[2:-2]
      word = word[-1]+word
      word = word[0:-1]
      return (word)

word = input("Enter a word: ")

coded = code(word)
print("The coded word is:", coded)

if(input("Enter 1 to decode or 0 to exit:") == '1'):
    decoded = decode(coded)
    print(decoded)
else:
   exit()
