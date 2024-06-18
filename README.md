## Introduction

- Vaccines-Africa project would like the Python program to show how many lives are saved by each vaccine (diphtheria , hepatitis B, measles, polio, rubella, tetanus, tuberculosis, yellow fever) on average in Africa from 2020, it can also calculate the annual surplus of unused vaccines. The calculations aim to estimate the vaccine production amount for next year.
- The total number of lives saved by each vaccine is calculated to give an insight into the number of lives saved by each type of vaccine. The program can calculate the total number of lives saved for the last 5 years. Data in the worksheet starts in the year of 2020.

<img width="866" alt="Screenshot 2024-06-17 at 15 11 36" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/eba3b0dd-6040-425a-acd1-29f05948068f">



## How this program works

1. Collect lives saved data from user
2. Check that the lives saved data entered by the user is valid, if not, messages will be displayed according to different issues to request the user to provide the correct format of the data.
3. Add lives saved data into the lives saved worksheet
4. Calculate surplus numbers (the number of each vaccine type produced minus the number of lives saved from last year.)
5. Add surplus data to the surplus worksheet
6. Calculate averages of the vaccine production numbers for the last 5 years
7. The vaccine company would like to save more lives by increasing the vaccine numbers, so a calculation of vaccine production numbers is added (using the averages of vaccine production numbers and adding 20% for next year)
8. Print vaccine production amount for recommendations and add data into the 'vaccineproduce' worksheet
9. Calculate the total number of lives saved for each vaccine from the past 5 years ( sum up the numbers of lives saved for each vaccine type)
10. Update data of the total lives saved numbers for each vaccine into the ’totallivessaved' worksheet


![vaccine_Africe_workflow](https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/0af6bc4d-6469-44a4-a52e-f0b80c4003f3)

## Features

- A welcome message and precise data entry instructions are displayed to inform users how and what to enter.
- Error messages and data issues would be displayed to inform users when invalid data is entered.
- Users must enter into the programme 8 numbers representing the number of lives saved in the last year. These 8 numbers are the lives saved by 8 different vaccines in the following order: diphtheria, hepatitis B, measles, polio, rubella, tetanus, tuberculosis, yellow fever.
- If valid data is entered, the number of lives saved will be updated in the 'livessaved' worksheet.
- Surplus figures for the last year are also calculated and updated in the 'surplus' worksheet.
- The amount of each vaccine for the next year is calculated and updated in the 'vaccineproduce' worksheet.
- The total number of lives saved over the last 5 years is calculated and updated in the 'totallivessaved' worksheet.
- If the data entered is valid, the following messages will be showned in the terminal:
  'Data is valid!', 'Updating livessaved worksheet...', 'livessaved worksheet updated successfully',
  'Calculating surplus data...', 'Updating surplus worksheet...', 'surplus worksheet updated successfully',
  'Caluculating vaccineproduce data', 'Updating vaccineproduce worksheet...', 'vaccineproduce worksheet updated successfully',
  'Calculating total lives saved data..', 'Updating totallivessaved worksheet...', 'totallivessaved worksheet updated successfully'

<img width="726" alt="Screenshot 2024-06-17 at 15 13 01" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/bd39f802-211a-4d11-a4a9-2f67fe1dd645">

<img width="730" alt="Screenshot 2024-06-17 at 15 14 16" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/3a1b4da1-107b-4882-8a8e-088ec0f3c96d">

## Testing 

 I have manually test this project by doing the following:
- Given invalid inputs: Error messages were displayed with differerent issues accordingly, e.g. too less or too many numbers; non-numerical data.
- Tested in my local terminal and the Code Institue Heroku terminal.


<img width="974" alt="Screenshot 2024-06-17 at 15 21 51" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/5299dad9-70c8-4760-b749-b59b07743713">



## Validtor Testing
+ PEP8
  - No errors were retirned from https://pep8ci.herokuapp.com/

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
+ Steps for deployment:
  - Get this repository ready to deploy
  - Create a new Heroku app
  - Set the buildbacks to `Python` and `NodeJs` in that order
  - Create a `Config Var` called `PORT`, and set this to `8000`
  - Create another `Config Var` called `CREDS` and pastes my JSON into the value field.
  - Link the Heroku app to the repository
  - Click on Deploy

## Credits
  - Some of the real data from this site was used in part to create this project. https://www.kaggle.com/datasets/willianoliveiragibin/vaccines-have-saved
  - The codes from the Love Sandwiches walking through project were used as a reference.
  - Code Institute for the deployment terminal

