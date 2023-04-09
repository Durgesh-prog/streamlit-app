import streamlit as st
import pandas as pd

st.write("""
# Find the largest

This app find the largest number among three numbers
""")
#Get Input

st.header('Input Parameters')

number1 = st.number_input("Number_1")
number2 = st.number_input("Number_2")
number3 = st.number_input("Number_3")

st.subheader('Prediction')
if number1 == 10:
    st.write('Approved')
else:
    st.write('Declined')

