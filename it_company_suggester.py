import streamlit as st

# Sample data for IT companies and their ratings (this can be expanded or fetched from a database/API)
companies = [
    {"name": "Google", "rating": 5},
    {"name": "Microsoft", "rating": 4.8},
    {"name": "Apple", "rating": 4.7},
    {"name": "Amazon", "rating": 4.5},
    {"name": "Facebook", "rating": 4.3},
    {"name": "Netflix", "rating": 4.2},
    {"name": "Adobe", "rating": 4.1},
    {"name": "Intel", "rating": 4.0},
]

def suggest_companies(rating):
    suggestions = [company["name"] for company in companies if rating <= company["rating"]]
    if not suggestions:
        suggestions = ["No companies match your criteria."]
    return suggestions

# Streamlit app
st.title("IT Company Suggester")

rating = st.slider("Enter your minimum rating:", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Suggest Companies"):
    st.write(f"Based on your rating of {rating}, we suggest the following companies:")
    suggestions = suggest_companies(rating)
    for company in suggestions:
        st.write(f"- {company}")
