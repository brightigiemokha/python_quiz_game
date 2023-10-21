print("Welcome to my Python Quiz!")

playing = input("Would you like to Play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Great Choice! Lets Play :)")

#Question 1
print("-------------------------")
print('What does CPU stands for?')
print("-------------------------")
print("A- Central Processing Unit")
print("B- Open Systems Interconnect")
print("C- Organised Stairway Interweb")
print("D- Open Safe Internet")
answer = input(" Answer : ")

if answer.lower() == "A":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is A")

#Question 2
print("-------------------------")
print('What is a Computer?')
print("-------------------------")
print("A- Computer is a software")
print("B- Open Systems Interconnect")
print("C- An Electronic device used in processing data")
print("D- An Internet device")
answer = input(" Answer : ")

if answer.lower() == "C":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is C")

#Question 3
print("-------------------------")
print('Who released their first antivirus product called VirusScan in 1987?')
print("-------------------------")
print("A- John wesley")
print("B- John McAfee")
print("C- Norton")
print("D- Bill Gate")
answer = input(" Answer : ")

if answer.lower() == "B":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is B")

#Question 4
print("-------------------------")
print('What word means to switch a computer off and on again?')
print("-------------------------")
print("A- Hibate")
print("B- Sleep")
print("C- Reboot")
print("D- shut down")
answer = input(" Answer : ")

if answer.lower() == "B":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is B")

#Question 5
print("-------------------------")
print('What term was coined by American John McCarthy in 1956?')
print("-------------------------")
print("A- John wesley")
print("B- John McAfee")
print("C- Norton")
print("D- Bill Gate")
answer = input(" Answer : ")

if answer.lower() == "B":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is B")

#Question 6
print("-------------------------")
print('Who developed Python Programming Language?')
print("-------------------------")
print("A- Wick van Rossum")
print("B-  Rasmus Lerdorf")
print("C- Guido van Rossum")
print("D- Niene Stom")
answer = input(" Answer : ")

if answer.lower() == "C":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is C")

#Question 7
print("-------------------------")
print('Which type of Programming does Python support?')
print("-------------------------")
print("A- object-oriented programming")
print("B- structured programming")
print("C- functional programming")
print("D- all of the mentioned")
answer = input(" Answer : ")

if answer.lower() == "D":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is D")

#Question 8
print("-------------------------")
print('Is Python case sensitive when dealing with identifiers?')
print("-------------------------")
print("A- no")
print("B- yes")
print("C- machine dependent")
print("D- none of the mentioned")
answer = input(" Answer : ")

if answer.lower() == "B":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is B")

#Question 9
print("-------------------------")
print('Which of the following is the correct extension of the Python file?')
print("-------------------------")
print("A- .python")
print("B- .pl")
print("C- .py")
print("D- .P")
answer = input(" Answer : ")

if answer.lower() == "C":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is C")

#Question 10
print("-------------------------")
print('Is Python code compiled or interpreted?')
print("-------------------------")
print("A- Python code is both compiled and interpreted")
print("B- Python code is neither compiled nor interpreted")
print("C- Python code is only compiled")
print("D- Python code is only interpreted")
answer = input(" Answer : ")

if answer.lower() == "A":
    print('Correct!, Well Done')
    score = score + 1
else:
    print("Incorrect answer, the answer is A")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing  unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect answer")
    print("Try again")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing  unit":
    print('Correct!')
    score = score + 1
else:
    print("Incorrect answer")
    print("Try again")

print ("You got " + str(score) + " questions correctly!")
print ("You got " + str((score / 4) * 100) + " %. ")