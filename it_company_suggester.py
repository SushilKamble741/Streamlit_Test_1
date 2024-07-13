import streamlit as st

# Sample data for IT companies and their review ratings
companies = [
    {"name": "Google", "rating": 4.8},
    {"name": "Microsoft", "rating": 4.5},
    {"name": "Apple", "rating": 4.7},
    {"name": "Amazon", "rating": 4.6},
    {"name": "Facebook", "rating": 4.2},
    {"name": "Netflix", "rating": 4.3},
    {"name": "Adobe", "rating": 4.4},
    {"name": "Intel", "rating": 4.1},
    {"name": "Salesforce", "rating": 4.0},
    {"name": "IBM", "rating": 3.8},
]

def suggest_companies(min_rating):
    suggestions = [company["name"] for company in companies if company["rating"] >= min_rating]
    if not suggestions:
        suggestions = ["No companies match your criteria."]
    return suggestions

# Streamlit app
st.title("IT Company Suggester Based on Review Ratings")

rating = st.slider("Enter your minimum review rating:", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Suggest Companies"):
    st.write(f"Based on your minimum rating of {rating}, we suggest the following companies:")
    suggestions = suggest_companies(rating)
    for company in suggestions:
        st.write(f"- {company}")
