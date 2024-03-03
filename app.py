import streamlit as st
from model import train_and_evaluate_model, predict_story_points

st.title('Scrum Team Story Points & Completion Prediction')

# Load and train the model
model = train_and_evaluate_model()

# User inputs
st.header('Enter Sprint Details:')
days_since_first_sprint = st.number_input('Days Since First Sprint', min_value=0)
leave = st.number_input('Leave', min_value=0)
working_days = st.number_input('Working Days', min_value=1)
availability = st.number_input('Availability', min_value=0.0, max_value=10.0, step=0.5)

if st.button('Predict Story Points and Completion'):
    story_points, story_completed = predict_story_points(model, days_since_first_sprint, leave, working_days, availability)
    st.success(f'Predicted Story Points: {story_points}, Predicted Story Completion: {story_completed}')
