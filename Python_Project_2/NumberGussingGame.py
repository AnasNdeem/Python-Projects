import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
      top_of_range = int(top_of_range)

      if top_of_range <= 0:
        print("Please write number larger than 0 next time.")
        quit()
else:
      print("PLease write a number next time.")
      quit()

random_number = random.randint(0, top_of_range)
guesses = 0 
while True:
     guesses += 1
     user_guess = input("Make a Guess:")
     if user_guess.isdigit():
      user_guesse = int(user_guess)

     else:
          print("PLease write a number next time.")
          continue
     
    
     if user_guess == random_number:
       print("You got it!")
       break
     else:
         if user_guesse > random_number:
             print("You are above the number!")
         else:
             print("You were below the number!")
       
   
print("You got it", guesses, "Guesses!")