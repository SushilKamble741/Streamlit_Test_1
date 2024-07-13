import streamlit as st

# Sample data for top universities (this can be expanded or fetched from a database/API)
universities = [
    {"name": "Harvard University", "min_percentage": 90},
    {"name": "Stanford University", "min_percentage": 85},
    {"name": "MIT", "min_percentage": 88},
    {"name": "Caltech", "min_percentage": 87},
    {"name": "University of Oxford", "min_percentage": 92},
]

def suggest_universities(percentage):
    suggestions = [uni["name"] for uni in universities if percentage >= uni["min_percentage"]]
    if not suggestions:
        suggestions = ["No universities match your criteria."]
    return suggestions

# Streamlit app
st.title("University Suggester")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
percentage = st.number_input("Enter your percentage:", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Suggest Universities"):
    if not name:
        st.warning("Please enter your name.")
    elif age <= 0:
        st.warning("Please enter a valid age.")
    elif percentage <= 0 or percentage > 100:
        st.warning("Please enter a valid percentage.")
    else:
        st.write(f"Hello, {name}! Based on your percentage of {percentage}%, we suggest the following universities:")
        suggestions = suggest_universities(percentage)
        for uni in suggestions:
            st.write(f"- {uni}")
