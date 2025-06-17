# Importing Streamlit, the package used for displaying the website
import streamlit as st

# Importing pandas
import pandas as pd

# Markdown: Introduction
st.write("""
# Introduction   
         
The project aims to use [Nasa's Exoplanet Data](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS) and anylizes it to make useful comparisons:
""")

# Importing the bare nasa data file
nasa_data = pd.read_csv("planetory_systems.csv", comment="#")

# Importing clean data
clean_data = pd.read_csv("data/data.csv")

# Displaying the dataframe
st.write(nasa_data)

# Markdown: Introducing Clean data
st.write("""
It uses ```analysis.ipynb``` to convert it into useful & required data:
         """)

st.write(clean_data)

# Markdown: Further Introduction
st.write("""
It then further analyses the data and converts it to useful partitions:

- ```👉 Comparing Planets Mass against Radius```
- ```👉 Compaing Stars Temperature against it's Planets Temperature```
- ```👉 Comparing Years by exoplanet discoveries```
- ```👉 Comparing the Planets Radius against it's Orbital Period```         
""")