# Import streamlit, main package used for creating the site 
import streamlit as st

# Using pandas data analysis.
import pandas as pd

# Load in the data
plain_data = pd.read_csv("../../data/star_vs_planet_temperature.csv")

# Markdown: Introduction
st.write("""
# Introduction
Using ```star_vs_planet_temperature.ipynb``` the clean data file is converted into the required columns:   
           
    st_teff: The planets stars temperature (K)
    pl_eqt: The planets temperature (K)
""")

# Write the filtered dataframe
st.write(plain_data)

# Markdown: Further Introduction
st.write("""
Using streamlit's built in scatter chart function a scatter chart can be made:
         """)

# Displaying the data using streamlit's built in scatter chart function
st.scatter_chart(data=plain_data, x="st_teff",x_label="Stars Temperature (K)", y="pl_eqt", y_label="Planets Temperature (K)")

# Markdown: Key Observations
st.write("""
# Key Observations
## Hotter stars tend to have hotter planets
This makes sense as stars heat their planets. Though this rule is not perfect as they're are likely other metrics by which the planets temperature depends on.
         
## Ranges
On the Y axis, mostly all the data ranges from 200-2800K. The 200K bottom limit might be due to the physical limitations as the planets might be too cold to detect

## Variation
The dataset suggests that the planets temperature might be influenced by many other factors, not just the stars temperature:
- Orbital Distance
- Stars brightness
- Planetory Atmosphere

These might be some of the factors that in addition to the stars temperature, affect the planets temperature 
         """)
