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

if playing != "yes":
    quit()

print("Great Choice! Lets Play :)")

answer = input("What does CPU stand for? ")
if answer is == "central processing  unit":
    print('Correct!')
else:
    print("Incorrect answer")