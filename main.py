import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Global_Superstore.csv")

st.title("Business Dashboard")

# Filters
region = st.selectbox("Select Region", df['Region'].unique())
category = st.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == region) & (df['Category'] == category)]

# KPIs
st.subheader("Key Metrics")
st.write("Total Sales:", filtered_df['Sales'].sum())
st.write("Total Profit:", filtered_df['Profit'].sum())

# Top customers
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
st.subheader("Top 5 Customers")
st.bar_chart(top_customers)

# Sales chart
st.subheader("Sales by Sub-Category")
sales_chart = filtered_df.groupby('Sub-Category')['Sales'].sum()
st.bar_chart(sales_chart)