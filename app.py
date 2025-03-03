import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("All_Data_ASDA.csv")

# Display the first 5 rows
print(df.head())

