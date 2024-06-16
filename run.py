import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get livessaved figures input from the user.
    """
    while True:
        print("Please enter livessaved data from last year.")
        print("Data should be eight numbers, separated ba commas")
        print("Example: 1000,2000,3000,4000,5000,6000,7000,8000\n")

        data_str = input("Enter your data here: ") 
        livessaved_data = data_str.split(",")

        if validate_data(livessaved_data):
            print("Data is valid!")
            break
    return livessaved_data
    

def validate_data(values):
    """ 
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 8 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"Exactly 8 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(livessaved_row):
    """ 
    Compare lives saved number with vaccine produce number and calculate the surplus for each vaccine type.

    The surplus is defined as the lives saved figure subtracted from the vaccine produce number.
    """
    print("Calculating surplus data...\n")
    vaccineproduce = SHEET.worksheet("vaccineproduce").get_all_values()
    vaccineproduce_row = vaccineproduce [-1]
    
    surplus_data = []
    for vaccineproduce, livessaved in zip(vaccineproduce_row, livessaved_row):
        surplus = int(vaccineproduce) - livessaved
        surplus_data.append(surplus)

    return surplus_data
    


def main():
    """ 
    Run all program functions
    """
    data = get_livessaved_data()
    livessaved_data = [int(num) for num in data]
    update_worksheet(livessaved_data, "livessaved")
    new_surplus_data = calculate_surplus_data(livessaved_data)
    update_worksheet(new_surplus_data, "surplus")
    

print("Welcome to Vaccines Africa Data Automation")
main()

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
