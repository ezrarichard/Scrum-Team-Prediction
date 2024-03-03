import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_and_evaluate_model(data_path='ScrumML.csv'):
    # Load and prepare the dataset
    data = pd.read_csv(data_path)

    # Select features and target for the model
    features = ['Team', 'Leave', 'Working Days', 'Availability']
    targets = ['Story Points', 'Story Completed']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[targets], test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on the testing set and evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Uncomment the following line if you wish to print the model evaluation metrics
    # print(f'Model Evaluation\nMean Squared Error: {mse:.2f}\nR^2 Score: {r2:.2f}')

    return model

def predict_story_points(model, team, leave, working_days, availability):
    
    features = np.array([[team, leave, working_days, availability]])
    prediction = model.predict(features)
    story_points, story_completed = prediction[0]
    return round(story_points), round(story_completed)
