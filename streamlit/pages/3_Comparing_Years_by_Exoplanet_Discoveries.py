# Importing Streamlit, the package used for displaying the website
import streamlit as st

# Importing pandas
import pandas as pd

# Markdown: Introduction
st.write("""
# Introduction
This is one of the simple analysis. This just counts the amount of exoplanets discovered each year in the file ```exoplanet_discoveries_by_year.ipynb``` and displays it as a bar chart:
         """)
# Getting clean data of discovery years
data = pd.read_csv("data/exoplanet_discoveries_by_year.csv")

# Displaying the graph using streamlits built it bar chart function
st.bar_chart(data=data, x="disc_year", x_label="Discovery Year", y="count", y_label="Number of planets discovered")

# Markdown: Key Observations
st.write("""
## Key Observations
The graph shows an almost consistent **upwards** spike, meaning almost every year we've discovered more exoplanets than the year before.
         
2025 only has 30 exoplanets discovered while 2024 has the had 135. This might be due to the fact that the year hasn't ended but also new discovery data isn't available in the database *yet*.
         """)