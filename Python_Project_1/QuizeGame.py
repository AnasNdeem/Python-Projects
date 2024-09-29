print("Welcome to my computer!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
   quit()



print("Okay! Lets play :)")
score = 0

answer = input("What dose CPU stand for?")
if answer == "central processing unit":
      print("Correct")
      score += 1
else:
      print("Incorrect")

answer = input("What dose GPU stand for?")
if answer == "graphics processing unit":
      print("Correct")
      score += 1
else:
      print("Incorrect")

answer = input("What dose Ram stan for?")
if answer == "random access memory":
      print("Correct")
      score += 1
else:
      print("Incorrect")

answer = input("What dose PSU Stand For?")
if answer == "power supply unit":
      print("Correct")
      score += 1
else:
      print("Incorrect")

answer = input("What dose ROM stand for?")
if answer == "read only memory":
      print("Correct")
      score += 1
else:
      print("Incorrect")

print("You got" + str(score) + "questions correct!")
print("You got" + str((score/4) * 100) + "%.")

"""
answer = input("")
if answer == "":
      print("Correct")
else:
      print("Incorrect")

answer = input("")
if answer == "":
      print("Correct")
else:
      print("Incorrect")

answer = input("")
if answer == "":
      print("Correct")
else:
      print("Incorrect")
"""
