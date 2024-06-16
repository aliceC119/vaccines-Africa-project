import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Vaccines - Africa (2020-2024)')

def get_livessaved_data():
    """ 
    Get livessaved figures input from the user
    """
    print("Please enter livessaved data from last year.")
    print("Data should be eight numbers, separated ba commas")
    print("Example: 1000,2000,3000,4000,5000,6000,7000,8000\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_livessaved_data()

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
