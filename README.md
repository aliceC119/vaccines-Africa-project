![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

## Purpose of this project

- Vaccines-Africa wants the Python programme to show how many lives are saved by each vaccine (diphtheria ,hepatitis B, measles , polio, rubella, tetanus, tuberculosis, yellow fever) on average in Africa from 2020.
- The usage of these averages help to decide how many vaccines to produce for the next year.
- The total number of lives saved by each of the vaccine can be shown. The programme can calculate the lump sum of lives saved numbers for the past 5 years starts from year 2020..

## How this program works

1. Collect lives saved data from user
2. Check that the lives saved data entered by the user is valid, if not, messages will be displayed according to different issues to request the user to provide the correct format of the data.
3. Add lives saved data into lives saved worksheet
4. Calculate surplus numbers (the number of vaccine produce minus the number of lives saved)
5. Add surplus data to surplus worksheet
6. Calculate averages of the vaccine production numbers for the last 5 years
7. User would like to increase lives save by vaccines numbers, so a calculation of vaccine production numbers is added (using the averages of vaccine prodction numbers and add 20% for next year)
8. Print vaccine production amount for recommendations and add data into 'vaccineproduce' worksheet
9. Calculate the total number of lives saved for each vaccine from the past 5 years ( sum up the numbers of lives saved for each vaccine)
10. Print the total lives saved numbers for each vaccine and add data into 'totallivessaved' worksheet

