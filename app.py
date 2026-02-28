
import random
vvvvv=random.randint(1,10)
guesshistory=[]
ask=int(input("What is your number"))
guesshistory.append(ask)
print(guesshistory)
while ask!=vvvvv:
       print(guesshistory)
       if ask<vvvvv:
              ask=int(input("try again HIGHER"))
              guesshistory.append(ask)
       if ask>vvvvv:
              ask=int(input("try again LOWER"))
              guesshistory.append(ask)
print("You got it! Your previous guesses:")
for i in range(1):
       print(guesshistory)



                
        


        
       

        

