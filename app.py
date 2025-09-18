import streamlit as st
import joblib

# Load the trained model and vectorizer
vectorizer=joblib.load("vectorizer.jb")
model=joblib.load("lr.model.jb")


# App title
st.title("FAKE NEWS DETECTION")
st.write("This is a simple fake news detection app. Enter the news text below to check if it's real or fake.")

# User input
news_input = st.text_area("News article:", "")

# Prediction
if st.button("Check News"):
    if news_input.strip():  # Ensure user entered some text
        # Transform input using the same vectorizer
        transform_input = vectorizer.transform([news_input])

        # Predict using the trained model
        prediction = model.predict(transform_input)

        # Show result
        if prediction[0] == 1:
            st.success("The news is Real")
        else:
            st.error("The news is Fake")
    else:
        st.warning("Please enter some news text to check.")
