
![EzraRichard_Banner (4)](https://github.com/ezrarichard/Scrum-Team-Prediction/assets/125721936/2da64a68-bdb4-4184-a7df-328dbfcb6c67)

# Scrum Team Story Points & Completion Prediction App

## Overview
This application leverages machine learning to predict the number of story points a Scrum team can complete in a future sprint, based on historical data. By inputting details about the team size, leaves, working days, and availability, users can get an estimate of the story points and the actual completion rate to better plan their sprint activities.

## How to Use
### Step 1: Setup
Ensure you have Python installed on your system.
Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt in your terminal.

### Step 2: Running the App
Open your terminal and navigate to the cloned repository's directory.
Start the Streamlit app by running streamlit run app.py.
The app should now be running in your default web browser.


### Step 3: Uploading Data
Once the app is running, you'll be prompted to upload a CSV file containing your Scrum team's historical data.
The CSV file should follow a specific format. You can download the CSV template directly from the app to ensure compatibility.

### Step 4: Training the Model
After uploading your CSV file, click the "Train Model with Uploaded Data" button to train the prediction model on your data.
The app will notify you once the model is trained successfully.

### Step 5: Making Predictions
With the model trained, you'll be able to input details for prediction:

Sprint Date: The date of the sprint for which you want to make a prediction.
Team Size: The number of team members participating in the sprint.
Leave: The number of leave days taken by team members during the sprint.
Working Days: The total number of working days in the sprint.
Availability: The overall availability of the team during the sprint, measured as a percentage.
Fill in these details and click "Predict Story Points and Completion" to receive your prediction.

## Important Notes
The accuracy of predictions depends on the quality and relevance of the historical data provided.
This app is designed as a tool to aid sprint planning and should be used in conjunction with expert judgment and team discussions.

## App
https://scrum-team-prediction.streamlit.app/

By providing an easy-to-use interface and a straightforward prediction process, this app aims to support Scrum teams in their sprint planning efforts, helping them set more accurate and achievable goals.

## Support
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow.svg)](https://www.buymeacoffee.com/ezrarichard)
