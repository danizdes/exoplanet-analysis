# Import streamlit, main package used for creating the site 
import streamlit as st

# Using pandas, numpy for data analysis. and matplotlib for diplaying the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
plain_data = pd.read_csv("../data/planet_radius_vs_mass.csv")

# Cleaning and transforming the data
data = plain_data[['pl_rade', 'pl_bmasse']].dropna()
data = plain_data[(data['pl_rade'] > 0) & (data['pl_bmasse'] > 0)]

# Convert the data to logorithmic data
data['log_radius'] = np.log10(data['pl_rade'])
data['log_mass'] = np.log10(data['pl_bmasse'])

# Drop Original Columns
data = data.drop("pl_rade", axis=1)
data = data.drop("pl_bmasse", axis=1)

# Plot using matplotlib
fig, ax = plt.subplots()
ax.scatter(data['log_radius'], data['log_mass'], alpha=0.5, s=10)
ax.set_xlabel("Log(Radius) [log10 Earth radii]")
ax.set_ylabel("Log(Mass) [log10 Earth masses]")
ax.set_title("Planet Radius vs Mass (Log-Log Scale)")
ax.grid(True)

# Markdown: Introduction
st.write("""
# Introduction
Using ```planet_mass_vs_radius.ipynb``` the clean data file is converted into the required columns:   
           
    pl_rade: The planets radius compared to earth
    pl_bmasse: The planets mass compared to earth
         
""")

# Write the raw clean data
st.write(plain_data)

# Markdown: Using Logorithmic data
st.write("""
We'll be using logorithmic functions for both the x and y axis as both data points span vast amounts of data, hence why compressing the data is needed:
         """)

# Write logorithmic clean data
st.write(data)

# Introduction: Introducing the graph
st.write("We'll be using MatPlotLib's scatter graph function to properly display the logorithmic data:")

# Writing matplotlib's logorithmic data
st.pyplot(fig)

# Markdown: Key Observations
st.write("""
# Key observations
## Relationship       
The data here suggests a **power-law** relationship as the logorithmic graph appears as a straight line:
         """)

# Adding the power-law relationship using latex
st.latex("M \propto R^k")

# Continuing key observations
st.write("""
Where:
         
    * M 👉 Mass
    * R 👉 Radius
    * k 👉 A constant for each planet telling us how mass increases with radius
         """)

# Markdown: Second observation
st.write("""
## Grouping of the data
The second observation noticed was how there were 2 groups of data, with a middle region:

### Group 1: Smaller radius and mass
These are likely **rocky planets** like earth or mars
   
### Group 2: Larger radius and mass
These are likely gas or ice giants like jupiter or saturn
         
### Middle Region
This is the transitional zone between the 2 groups
         
This shows a **clear physical division** in planet types.  
""")