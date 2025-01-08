# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:02:20 2025

@author: himanshu.pant
"""

# Import modules
import streamlit as st
import pandas as pd

# Image URL
image_url = "https://i.cdn.newsbytesapp.com/images/l91120240815160849.png"

# Title
st.title("VE Dashboard")

# Display the image
st.image(image_url, width=500, caption="BIC", use_column_width=True)

# Header
st.header("Cell Design Team") 

# Subheader
st.subheader("Comparision Data")

# File upload widget
uploaded_file = st.file_uploader("Chose the excel file", type="xlsx")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the Excel file using pandas
    df = pd.read_excel(uploaded_file)
    
    # Display the DataFrame in the Streamlit app
    st.write("Here is the data from your Excel file:")
    st.dataframe(df)  # You can also use st.table(df) for a static table

else:
    st.warning("Please upload an Excel file to see the data.")

