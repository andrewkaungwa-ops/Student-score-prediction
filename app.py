import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("student_score_model.pkl", "rb"))

st.title("🎓 Student Score Predictor")

num_features = model.n_features_in_

inputs = []
for i in range(num_features):
    value = st.slider(f"Feature {i+1}", 0, 100, 50)
    inputs.append(value)

if st.button("Predict Score"):
    input_data = np.array([inputs])
    predicted_score = model.predict(input_data)
    score = predicted_score[0]

    st.subheader(f"Predicted Score: {score:.2f}")
    st.progress(int(score))
