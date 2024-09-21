import streamlit as st
import pandas as pd
import numpy as np
st.title('Public Transportation in Lebanon')
st.write('Showing the different means of transportation and different condition of roads in Lebanese Governates')

# Load your dataset
data = pd.read_csv('/Users/walidaboulhosn/Downloads/Transportation.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Distribution of Different Means of Transportation Among Governates')

# Convert the governorate links to a more readable form by extracting the last part of the URL
data['Governorate'] = data['refArea'].apply(lambda x: x.split('/')[-1].replace('_', ' '))

# Selector for the type of transportation
transport_type = st.selectbox(
    'Select the type of transportation',
    ['buses', 'taxis', 'vans']
)

# Prepare the data for plotting
if transport_type == 'buses':
    column_name = 'The main means of public transport - buses'
elif transport_type == 'taxis':
    column_name = 'The main means of public transport - taxis'
else:
    column_name = 'The main means of public transport - vans'

# Create a bar chart
st.bar_chart(data.groupby('Governorate')[column_name].sum())

st.subheader('State of Different Roads depending on their Type')
# Dropdown for selecting road condition
road_condition_columns = [col for col in data.columns if 'State of' in col]
selected_condition = st.selectbox("Select a Road Condition", road_condition_columns)

# Display the distribution of the selected road condition
st.write(f"Distribution of {selected_condition}:")
condition_counts = data[selected_condition].value_counts()
st.bar_chart(condition_counts)

st.write('Thank you! These visuals provide us with insights on the distribution of different means of transporation, as well as road conditions and the initiatives in different governates')
