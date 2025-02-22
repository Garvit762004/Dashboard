import streamlit as st
import pandas as pd

# Load data from published Google Sheets CSV
DATA_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSgbuUeZzFreMO2mh_MkO3IBJw9ykOngNWyLSqFRcYRYBnacaD-3_IN8y-6ASatD-gpZzcTHfPw2VTp/pub?output=csv'

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df['Application Status'] = df['Application Status'].astype(str)  # Ensure it's treated as string
    return df

def main():
    st.title("Recruitment Dashboard 📊")

    # Load Data
    df = load_data()

    # Total People
    total_people = len(df)

    # Screening: Include both 'Interview Scheduled' and 'Resume Shortlisted'
    screening = df[df['Application Status'].str.contains("Interview Scheduled|Resume Shortlisted", case=False, na=False)]

    # Rejected
    rejected = df[df['Application Status'].str.contains("Rejected", case=False, na=False)]

    # Offer Given
    offer_given = df[df['Application Status'].str.contains("Offer", case=False, na=False)]

    # Display Metrics
    st.metric("👥 Total People", total_people)
    st.metric("🧐 In Screening", len(screening))
    st.metric("❌ Rejected", len(rejected))
    st.metric("🎉 Offers Given", len(offer_given))

    # Optional: Display raw data
    if st.checkbox("Show Raw Data"):
        st.write(df)

if __name__ == "__main__":
    main()
