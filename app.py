import streamlit as st
import pandas as pd
from model import train_and_evaluate_model, predict_story_points

st.title('Scrum Team Story Points & Completion Prediction')

# Template download
st.markdown("### Download Input Template")
template_data = pd.DataFrame({
    'Sprint Date': ['2022-01-01'],  # Example date format
    'Team': [8],
    'Leave': [0], 
    'Working Days': [20], 
    'Availability': [7.5],
    'Story Points': [44],  # Example value
    'Story Completed': [42]  # Example value
})
csv = template_data.to_csv(index=False)
st.download_button(
    label="Download CSV Template",
    data=csv,
    file_name='scrum_input_template.csv',
    mime='text/csv',
)

# File uploader
uploaded_file = st.file_uploader("Upload your input CSV file for training", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded dataset
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Dataset Preview:")
    st.dataframe(data.head())  # Show a preview of the uploaded dataset

    if st.button('Train Model with Uploaded Data'):
        # Train the model on the uploaded dataset
        model = train_and_evaluate_model(data)
        st.success('Model trained successfully on the uploaded data. Now, provide details for prediction.')

        # Now ask for user inputs for prediction
        st.header('Enter Details for Prediction:')
        sprint_date = st.date_input('Sprint Date')  # Collects a date
        team = st.number_input('Team Size', min_value=1, max_value=20)  # Assuming team size ranges from 1 to 20
        leave = st.number_input('Leave', min_value=0)
        working_days = st.number_input('Working Days', min_value=1)
        availability = st.number_input('Availability', min_value=0.0, max_value=10.0, step=0.5)

        if st.button('Predict Story Points and Completion'):
            # Predict using the inputs
            story_points, story_completed = predict_story_points(model, team, leave, working_days, availability)
            st.success(f'Predicted for Sprint Date {sprint_date}: Story Points: {story_points}, Story Completion: {story_completed}')
else:
    st.write("Please upload a CSV file to proceed.")
