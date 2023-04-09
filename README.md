# Workout_tracker
This allows you to track your workouts and calculate your burned calories. 
The app uses APIs from https://developer.nutritionix.com/ to calculate calories burned, time, 
and type of exercise; and from sheety.co to create a table with all your workouts.

Technical.
The program is written in Python and utilizes the requests and json modules to make API calls and parse the returned JSON data. 
The program uses environment variables to store API keys and other sensitive information, ensuring that they are not exposed in the code.

The program logs into the Nutritionix API and retrieves data on the calories burned during a workout. 
It then posts this data to a Google Sheets document using the Sheety API.

Usage.
The program prompts the user to input the type of workout they did that day. Based on the input, the program makes a 
POST request to the Nutritionix API to retrieve data on the calories burned. 
It then formats this data and posts it to a Google Sheets document using the Sheety API.

Features.
Queries the Nutritionix API to calculate the calories burned during a workout
Posts data to a Google Sheets document using the Sheety API
Uses environment variables to store sensitive information and API keys
Easy-to-use user interface that prompts the user for inpu
