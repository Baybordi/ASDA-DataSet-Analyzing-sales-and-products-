import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Set Streamlit page config
st.set_page_config(layout="wide", page_title="ASDA Data Dashboard")

# ✅ Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("D:/negar/Middlesex uni/Data sets/ASDA/All_Data_ASDA.csv", 
                     dtype={'own_brand': str},
                     low_memory=False)
    df = df.head(5000)  # Load only 5000 rows for speed
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df


df = load_data()

# ✅ Display dataset (optional)
st.write("### First 5 rows of the dataset")
st.write(df.head())

# ✅ Bar Chart: Sales by Category
st.write("### Sales by Category")
fig_bar = px.bar(df, x="category", y="prices_(£)", title="Total Sales for Each Category")
st.plotly_chart(fig_bar, use_container_width=True)

# ✅ Line Chart: Sales Over Time
st.write("### Sales Over Time")
fig_line = px.line(df, x="date", y="prices_(£)", title="Sales Trend Over Time")
st.plotly_chart(fig_line, use_container_width=True)
