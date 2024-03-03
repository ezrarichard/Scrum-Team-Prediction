import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_and_evaluate_model(data):
    """
    Trains and evaluates a linear regression model based on the provided DataFrame.

    Parameters:
    - data (DataFrame): The dataset to train the model on, expected to have specific columns.

    Returns:
    - model (LinearRegression): The trained linear regression model.
    """
    # Ensure the data is a DataFrame, useful when the function is called with a file path or a DataFrame
    if isinstance(data, str):
        data = pd.read_csv(data)

    # Select features and targets for the model
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

    # Optional: Print the model evaluation metrics
    # print(f'Model Evaluation\nMean Squared Error: {mse:.2f}\nR^2 Score: {r2:.2f}')

    return model

def predict_story_points(model, team, leave, working_days, availability):
    """
    Predicts story points and story completion based on the provided sprint details.

    Parameters:
    - model (LinearRegression): The trained model.
    - team (int): The team size.
    - leave (int): The number of leaves.
    - working_days (int): The number of working days.
    - availability (float): The availability score.

    Returns:
    - tuple: Predicted story points and story completion, both rounded to the nearest integer.
    """
    features = np.array([[team, leave, working_days, availability]])
    prediction = model.predict(features)
    story_points, story_completed = prediction[0]
    return round(story_points), round(story_completed)
