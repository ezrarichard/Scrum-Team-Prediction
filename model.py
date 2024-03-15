import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

def train_and_evaluate_model(data):
    """
    Trains and evaluates a linear regression model based on the provided DataFrame.

    Parameters:
    - data (DataFrame): The dataset to train the model on, expected to have specific columns.

    Returns:
    - model (LinearRegression): The trained linear regression model.
    """
    if isinstance(data, str):
        data = pd.read_csv(data)

    # Select features and targets for the model
    features = ['Team', 'Leave', 'Working Days', 'Availability']
    targets = ['Story Points', 'Story Completed']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[targets], test_size=0.2, random_state=42)

    # Initialize a scaler using the training data
    scaler = StandardScaler().fit(X_train)

    # Scale the features
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the linear regression model on the scaled training data
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predict on the scaled testing set and evaluate the model
    predictions = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return model, scaler # Return both the model and the scaler

def predict_story_points(model, scaler, team, leave, working_days, availability):
    """
    Predicts story points and story completion based on the provided sprint details.

    Parameters:
    - model (LinearRegression): The trained model.
    - scaler (StandardScaler): The scaler used for feature scaling.
    - team (int): The team size.
    - leave (int): The number of leaves.
    - working_days (int): The number of working days.
    - availability (float): The availability score.

    Returns:
    - tuple: Predicted story points and story completion, both rounded to the nearest integer.
    """
    features = np.array([[team, leave, working_days, availability]])
    # Scale the features using the same scaler used during training
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    story_points, story_completed = prediction[0]
    return round(story_points), round(story_completed)
