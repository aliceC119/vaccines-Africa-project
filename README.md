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
8. Calculate averages of the vaccine production numbers for the last 5 years
9. The vaccine company would like to save more lives by increasing the vaccine numbers, so a calculation of vaccine production numbers is added (using the averages of vaccine production numbers and adding 20% for next year)
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


- If valid data is entered, a message of 'Data is valid!' will be shown. Also the numbers of lives saved will be updated in the 'livessaved' worksheet and the provided data will be displayed in the terminal.
   <img width="730" alt="Screenshot 2024-06-19 at 02 18 41" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/15c567c5-8569-42ee-bac5-7e3b9f4c84b3">
  
  <img width="836" alt="Screenshot 2024-06-19 at 02 36 00" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/2d5909d6-afad-4ac7-a7d3-9d3ffbd906df">


- Surplus figures for the last year will be also calculated and updated in the 'surplus' worksheet. The calculated surplus numbers will be displayed in the terminal.
  
  <img width="730" alt="Screenshot 2024-06-19 at 02 22 50" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/f41d2829-dab1-40a0-ac6a-0cf37964da45">
  <img width="853" alt="Screenshot 2024-06-19 at 02 37 32" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/af84d48f-077f-432f-8409-845d943b02b2">
  
  

- The amounts of each vaccine for the next year will be calculated and updated in the 'vaccineproduce' worksheet. The calculated vaccine production numbers will be displayed in the terminal.
  <img width="631" alt="Screenshot 2024-06-19 at 02 26 57" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/9c95949a-280a-4a67-b593-7bf6ae3c2f0f">
  <img width="850" alt="Screenshot 2024-06-19 at 02 40 20" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/881371ad-1925-4974-bbae-7214b2a2ad56">


- The total number of lives saved over the last 5 years will be calculated and updated in the 'totallivessaved' worksheet. The calculated numbers of total lives saved will be displayed in the terminal.
  <img width="728" alt="Screenshot 2024-06-19 at 02 29 16" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/5a8a6111-0313-44e7-a79d-2abefee87773">
  <img width="854" alt="Screenshot 2024-06-19 at 02 46 21" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/a86df032-fc77-489c-91d7-cc08171bd9be">


- At the end of the programme, a production list for each vaccine will be displayed for the next year according to the previously calculated vaccine production figures.
  
  <img width="729" alt="Screenshot 2024-06-19 at 02 33 39" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/f52761bf-d887-4d2b-8cc2-07d0a5859a4f">




## Testing 

 I have manually test this project by doing the following:
- Given invalid inputs: Error messages were displayed with differerent issues accordingly, e.g. too less or too many numbers; non-numerical data.
  <img width="856" alt="Screenshot 2024-06-19 at 02 53 33" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/460ff59f-aac9-4df3-ad8f-da60411e37da">
- Given valid inputs: A 'Data is valid' message will be displayed. The terminal will also display the calculated values of the data: surplus, vaccine production, total lives saved. At the end of the programme, a production list for each vaccine will be displayed for the next year according to the previously calculated vaccine production figures.
  <img width="927" alt="Screenshot 2024-06-19 at 03 02 18" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/d276672b-0cbe-4dde-8331-9685293ae564">

- The entered data and calculated data were updated in the spreadsheet.
  
  <img width="860" alt="Screenshot 2024-06-19 at 03 07 43" src="https://github.com/aliceC119/vaccines-Africa-project/assets/162838985/90700d90-111c-4e99-90c9-5eecdd383416">

  

- Tested in my local terminal and the Code Institue Heroku terminal.





## Validtor Testing
+ PEP8
  - No errors were returned from https://pep8ci.herokuapp.com/

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

