
import random
vvvvv=random.randint(1,10)
guesshistory=[]
ask=int(input("What is your number"))
guesshistory.append(ask)
while ask!=vvvvv:
       print(guesshistory)
       if ask<vvvvv:
              ask=int(input("try again HIGHER"))
              guesshistory.append(ask)
       if ask>vvvvv:
              ask=int(input("try again LOWER"))
              guesshistory.append(ask)
for i in guesshistory:
       print(f"You got it! Your previous guesses:{guesshistory}")




                
        


        
       

        

