## Introduction

- Vaccines-Africa project would like to show how many lives are saved by each vaccine (diphtheria , hepatitis B, measles, polio, rubella, tetanus, tuberculosis, yellow fever) in Africa in each year, it can also calculate the annual surplus of unused vaccines. The calculations aim to estimate the vaccine production amount for next year.
- The total number of lives saved by each vaccine is calculated to give an insight into the number of lives saved by each type of vaccine. The program can calculate the total number of lives saved for the last 5 years. Data in the worksheet starts in the year of 2020.
- The link directs to the app https://vaccine-africa-project-6752f2263f16.herokuapp.com/
<img width="1083" alt="Screenshot 2024-06-19 at 00 41 26" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/ea573253-06fa-4a7f-9f81-360ade5215eb">





## How this program works

1. Collect lives saved data from user
2. Check that the lives saved data entered by the user is valid, if not, messages will be displayed according to different issues to request the user to provide the correct format of the data.
3. Valid lives saved data will be displayed in the terminal after entered by the user.
4. Add lives saved data to the 'livessaved' worksheet.
5. Calculate surplus numbers (the number of each vaccine type produced minus the number of lives saved from last year.)
6. Calculated surplus data will be displayed in the terminal.
7. Add surplus data to the 'surplus' worksheet.
8. Calculate averages of the vaccine production numbers for the last 5 years.
9. The vaccine company would like to save more lives by increasing the vaccine numbers, so a calculation of vaccine production numbers is added (using the averages of vaccine production numbers and adding 20% for next year).
10. Calculated numbers of the vaccine production for next year will be displayed in the terminal.
11. Add data of the vaccine production to the 'vaccineproduce' worksheet.
12. Calculate the total number of lives saved for each vaccine from the past 5 years ( sum up the numbers of lives saved for each vaccine type)
13. Calculated numbers of the total lives saved will be displayed in the terminal.
14. Add the total number of lives saved for each vaccine to the 'totallivessaved' worksheet.
15. Request detailed production data showing the amount of each type of vaccine estimated to be produced for the next year.
16. A detailed vaccine production data list will be displayed on the terminal.
17. At the end of the program, a message is displayed thanking the user for using the program, informing the user that the data in the worksheets has been updated, and asking the user to enter new data.


![vaccine_Africe_workflow](https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/0af6bc4d-6469-44a4-a52e-f0b80c4003f3)

## Features

- A welcome message and precise data entry instructions are displayed to inform users how and what to enter.
- Users must enter into the programme 8 numbers representing the number of lives saved by the following 8 vaccines in the last year: Diphtheria, Hepatitis B, Measles, Polio, Rubella, Tetanus, Tuberculosis, Yellow fever.
   <img width="729" alt="Screenshot 2024-06-19 at 02 08 24" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/343ea4f6-16c8-43f9-b527-4561631c10ea">
 
- Error messages and their data issues would be displayed to inform users when invalid data is entered. Here is an example:
  
  <img width="729" alt="Screenshot 2024-06-19 at 02 15 19" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/c0e122ce-50f3-431b-9bd2-1171d6f28cdf">


- If valid data is entered, a message of 'Data is valid!' will be shown. Also the numbers of lives saved will be updated in the 'livessaved' worksheet.
  
   <img width="729" alt="Screenshot 2024-06-20 at 12 44 41" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/f2234cc7-b707-449d-a7c2-e9bd12f26ef2">
   
  <img width="850" alt="Screenshot 2024-06-20 at 12 58 38" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/fb33c55b-c13a-4959-96a8-fb3d738299e9">



- Surplus figures for the last year will be also calculated and updated in the 'surplus' worksheet. The new surplus numbers will be displayed on the terminal.
  
  <img width="729" alt="Screenshot 2024-06-20 at 12 59 55" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/ef507365-52bb-4822-8ac4-8daadbc7b1d4">


  <img width="850" alt="Screenshot 2024-06-20 at 13 01 00" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/e35119bd-e3eb-4944-8204-71d149e8b6f1">


- The amounts of each vaccine for the next year will be calculated and updated in the 'vaccineproduce' worksheet. The calculated vaccine production numbers will be displayed in the terminal.
  
  <img width="731" alt="Screenshot 2024-06-20 at 13 01 57" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/e5b2aa8d-d3d0-4e76-97a6-9d3f8ea2a819">

   <img width="852" alt="Screenshot 2024-06-20 at 13 03 09" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/9e29a6fd-79c0-4ebd-b728-ed20e76bfe9b">

- The total number of lives saved over the last 5 years will be calculated and updated in the 'totallivessaved' worksheet. The calculated numbers of total lives saved will be displayed in the terminal.
 
  <img width="730" alt="Screenshot 2024-06-20 at 13 04 21" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/d673272a-b81d-49ca-a554-1df5c5598d78">

  <img width="850" alt="Screenshot 2024-06-20 at 13 05 14" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/18e39f98-8f05-4236-8160-70f8b481ece9">


- At the end of the programme, a production list for each vaccine will be displayed for the next year according to the previously calculated vaccine production figures.
  
  <img width="729" alt="Screenshot 2024-06-19 at 02 33 39" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/f52761bf-d887-4d2b-8cc2-07d0a5859a4f">

- At the end of the program, a message is displayed thanking the user for using the program, informing the user that the data in the worksheets has been updated, and asking the user to enter new data.

  <img width="730" alt="Screenshot 2024-06-20 at 13 06 23" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/e3951676-f6f1-454d-8c59-b2055c413d1f">





## Testing 

 I have manually test this project by doing the following:
- Given invalid inputs: Error messages were displayed with differerent issues accordingly, e.g. too less or too many numbers; non-numerical data.
  
  <img width="856" alt="Screenshot 2024-06-19 at 02 53 33" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/460ff59f-aac9-4df3-ad8f-da60411e37da">
  
- Given valid inputs: A 'Data is valid' message will be displayed. The terminal will also display the calculated values of the data: surplus, vaccine production, total lives saved. At the end of the programme, a production list for each vaccine will be displayed for the next year according to the previously calculated vaccine production figures.
  
  <img width="990" alt="Screenshot 2024-06-20 at 13 11 06" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/593e3de9-2560-4ec2-b9d4-49128d54417f">


- The entered data and calculated data were updated in the spreadsheet.
  
  <img width="860" alt="Screenshot 2024-06-19 at 03 07 43" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/90700d90-111c-4e99-90c9-5eecdd383416">

- Tested in my local terminal and the Code Institue Heroku terminal.

## Validtor Testing
+ PEP8
  - No errors were returned with the codes from the Gitpod Workspace from https://pep8ci.herokuapp.com/
    
## Error relates to the validation
  - No error was found when validating the codes from the Gitpod workspace, however,
a format error of no new line was found when validating the codes from the Github file.

   <img width="678" alt="Screenshot 2024-06-20 at 13 27 35" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/9524f5dc-371d-4bea-9fbf-70ad2baae51f">

   <img width="674" alt="Screenshot 2024-06-20 at 13 30 18" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/e901e651-6323-4309-bae8-678ca6f9c351">


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

