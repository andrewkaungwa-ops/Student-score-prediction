import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("student_score_model.pkl", "rb"))

st.title("Student Score Prediction System")

study_hours = st.number_input("Weekly Self Study Hours")
absence_days = st.number_input("Absence Days")

if st.button("Predict Score"):

    prediction = model.predict([[study_hours, absence_days]])
    score = prediction[0]

    st.subheader("Predicted Final Score:")
    st.write(round(score,2))

    if score < 60:
        st.write("Recommendation: Increase study hours and reduce absences.")
    elif score < 80:
        st.write("Recommendation: Good performance but more study could improve scores.")
    else:
        st.write("Excellent performance. Keep it up!")