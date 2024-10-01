import random
import time

OPREATORS = ['+', '-',"*"]
MIN_OPERAND = 3
MAX_OPRAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
   left = random.randint(MIN_OPERAND, MAX_OPRAND)
   right = random.randint(MIN_OPERAND, MAX_OPRAND)
   operator = random.choice(OPREATORS)

   expr = str(left) + " " + operator + " " + str(right)
   answer = eval(expr)
   return expr, answer

wrong = 0
input("Press enter to start!")
print("--------------------")

start_time = time.time()

for i in range (TOTAL_PROBLEMS):
   expr, answer = generate_problem()
   while True:
      guess = input("Problem #" + str(i + 1) + ": " + expr + "=")
      if guess == str(answer):
        break
      wrong += 1

end_time = time.time()
total_time = end_time - start_time


print("--------------------")
print("NICE WORK! You finishied in", total_time, "Seconds")