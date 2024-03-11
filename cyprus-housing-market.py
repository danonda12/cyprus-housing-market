import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setup and configurations
st.set_page_config(page_title="Cyprus Housing Market Insights", layout="wide")

# Data Loading
def generate_data():
    np.random.seed(0)  # Seed for reproducibility
    locations = ['Nicosia', 'Limassol', 'Paphos', 'Larnaca']
    types = ['Apartment', 'Villa']
    data = {
        'Type': np.random.choice(types, 100),
        'Location': np.random.choice(locations, 100),
        'Price': np.random.randint(100000, 2000000, 100),  # Prices between 100k and 2M
        'Amenities': np.random.choice(['Beachfront', 'Mountain View', 'City Life', 'Rural Retreat'], 100)
    }
    return pd.DataFrame(data)

df = generate_data()
st.sidebar.markdown("**Note:** This app uses simulated data for demonstration purposes.")
# User Interface Components
st.title('Cyprus Housing Market Insights')
st.write('Explore the diverse and vibrant housing market of Cyprus, from bustling cities to serene coastal villages.')

st.header('Search for Properties')
with st.sidebar:
    selected_type = st.selectbox('Select Property Type', df['Type'].unique())
    selected_location = st.selectbox('Select Location', df['Location'].unique())
filtered_df = df[(df['Type'] == selected_type) & (df['Location'] == selected_location)]

st.write('Properties Found:', filtered_df.shape[0])
st.dataframe(filtered_df)

# Visualization
st.header('Price Trends')
fig, ax = plt.subplots()
ax.hist(df['Price'], bins=20, color='skyblue')
ax.set_title('Property Price Distribution')
ax.set_xlabel('Price')
ax.set_ylabel('Number of Properties')
st.pyplot(fig)

# Running the app: Save this script as `cyprus_housing_app.py` and run it using the command:
# streamlit run cyprus_housing_app.py
