import random
import time

low = 0
high = 10
mode = input("Pick level.\n1 is easy.\n2 is mid.\n3 is hard.\n")
if mode == "1":
  print("Easy mode has been selected.")

elif mode == "2":
  print("Mid mode has been selected.")
  low = 0
  high = 100

elif mode == "3":
  print("High mode has been selected.")
  low = 10
  high = 1000
else:
  print("Default mode : Easy has been selected.")

operators = ["+", "-", "*", "/"]

score = 0
total = input("How many questions do you want?\n")
if total.isnumeric():
  total = int(total)
else:
  print("Defalt number of questions has been picked, which is 10.")
  total = 10

print("You have", total, "questions.")

start = time.time()

for i in range(total):
  operator = random.choice(operators)
  firstNumber = random.randint(low, high)
  secondNumber = random.randint(low, high)
  question = str(firstNumber) + operator + str(secondNumber)
  correct_answer = eval(question)

  print(f"Question {i+1} : What is {question}?")

  answer = input()

  if answer.isnumeric():
    answer = int(answer)
  else:
    print("Invalid answer.")
    continue

  if answer == correct_answer:
    print("Correct answer!")
    score = score + 4

  else:
    print("Incorrect answer.")
    score = score - 1

end = time.time()

time_taken = round(end - start, 2)
print("Time taken was\n", time_taken)
avgTime = time_taken / total
print("Your average time was.\n", avgTime)

print("Your score was:", score, "/", total * 4)
