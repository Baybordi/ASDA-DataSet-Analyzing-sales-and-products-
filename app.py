import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv("All_Data_ASDA.csv")

# Display the first 5 rows in the terminal (optional)
print(df.head())

# ❌ Fix error: `wide` should be a string ('wide')
st.set_page_config(layout="wide")  

# Load and display image
image = Image.open("asda.png")
col1, col2 = st.columns([0.9, 0.1])
with col2:
    st.image(image, width=100)
# Add custom styling for title
html_title = '''
  <style>
  .title_test {
   font-weight: bold;
   padding: 5px;
   border-radius: 6px;
   font-family:'BTitr';
  }
  </style>
  <center><h1 class="title_test">Business Dashboard</h1></center>
'''
with col1:
    st.markdown(html_title,unsafe_allow_html=True)
