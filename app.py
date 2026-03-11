import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("student_score_model.pkl", "rb"))

st.title("🎓 Student Score Predictor")

study_hours = st.slider("Study Hours per Day", 0, 12, 4)
attendance = st.slider("Attendance (%)", 0, 100, 75)

if st.button("Predict Score"):
    input_data = np.array([[study_hours, attendance/100]])
    predicted_score = model.predict(input_data)
    score = max(0, min(100, predicted_score[0]))

    st.subheader(f"Predicted Score: {score:.2f}")
    st.progress(int(score))

    if score < 60:
        st.error("⚠️ Student may fail. Increase study time.")
    elif score < 80:
        st.warning("📚 Student is doing okay but can improve.")
    else:
        st.success("🎉 Excellent performance predicted!")
        st.balloons()
