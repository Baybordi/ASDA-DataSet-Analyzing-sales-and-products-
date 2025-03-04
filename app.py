import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

# ✅ Set Streamlit page config at the very top
st.set_page_config(layout="wide")  

# Load dataset with caching
@st.cache_data
def load_data():
    return pd.read_csv("All_Data_ASDA.csv")

df = load_data()

# Convert date column to datetime and extract year
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Handle errors if any invalid dates
df['year'] = df['date'].dt.year

# Sort unique years for selection
years = sorted(df['year'].dropna().unique())  

# Display the first 5 rows in the terminal (optional)
print(df.head())

# Load and display image
image = Image.open("asda.png")
col1, col2 = st.columns([0.9, 0.1])
with col2:
    st.image(image, width=100)

# Custom title styling
html_title = """
  <style>
  .title_test {
   font-weight: bold;
   padding: 5px;
   border-radius: 6px;
   font-family:'BTitr';
  }
  </style>
  <center><h1 class="title_test">Business Dashboard</h1></center>
"""
with col1:
    st.markdown(html_title, unsafe_allow_html=True)

# Year selection filter
selected_year = st.selectbox('Select The Year', years)

# Filter data based on selected year
filtered_df = df[df["year"] == selected_year]

# Bar chart visualization
col3, col4 = st.columns([0.45, 0.45])
with col4:
    fig = px.bar(filtered_df, x="category", y="prices_(£)",  
                 labels={"prices_(£)": "Sales", "category": "Different Products"},
                 hover_data=["prices_(£)"],
                 height=500)
    fig.update_layout(
        title=f"Sales for {selected_year}",
        xaxis_title="Category of products",
        yaxis_title="Sales (£)",
        font=dict(family="Times New Roman")
    )
    st.plotly_chart(fig, use_container_width=True)
