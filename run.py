import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_game')

print("Welcome to my Python Quiz!")

playing = input("Would you live to Play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Great Choice! Lets Play :)")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing  unit":
    print('Correct!')
    score = score + 1
else:
    print("Incorrect answer")
    print("Try again")

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