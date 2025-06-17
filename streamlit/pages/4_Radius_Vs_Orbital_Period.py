# Import streamlit, main package used for creating the site 
import streamlit as st

# Using pandas data analysis.
import pandas as pd

# MatPlotLib to display graph
import matplotlib.pyplot as plt

# Numpy for logorithmic function
import numpy as np

# Importing the clean data file
plain_data = pd.read_csv("data/planets_radius_vs_orbper.csv")

## CODE STOLEN FROM MASS VS RADIUS :) ##

# Cleaning and transforming the data
data = plain_data[['pl_orbper', 'pl_rade']].dropna()
data = plain_data[(data['pl_orbper'] > 0) & (data['pl_rade'] > 0)]

# Convert the data to logorithmic data
data['log_pl_orbper'] = np.log10(data['pl_orbper'])

# Drop Original Column
data = data.drop("pl_orbper", axis=1)

# Plot using matplotlib
fig, ax = plt.subplots()
ax.scatter(data['log_pl_orbper'], data['pl_rade'], alpha=0.5, s=10)
ax.set_xlabel("Log(Orbital Period) [log 10]")
ax.set_ylabel("Radius [Compared to Earth Radii]")
ax.set_title("Planet Orbital Period vs Radii (Log Scale)")
ax.grid(True)

## CODE STOLEN FROM MASS VS RADIUS :) ##

# Markdown: Introduction
st.write("""
# Introduction
This compares the radius of the planet with it's orbital period. the orbital period has been compressed with logorithmic functions:
    """)

# Writing the new clean data
st.write(data)

# Markdown: Introducing Scatter Chart
st.write("Using MatPlotLib, we can affectively create a scatter chart:")

# Plot the figure
st.pyplot(fig)

# Markdown: Key Observations
st.write("""
# Key Observations
## Short orbital periods
Most planets have an orbital period of 1 to 100 days, which is very short compared to earth
## No strong correlation
There isn't any strong correlation between the planets radius and orbital period, suggesting that planet size is **not directly dependant** on orbital period
         """)