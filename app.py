import streamlit as st

st.write("""
# Find the largest

This app find the largest number among three numbers
""")
#Get Input

st.header('Input Parameters')

number1 = st.number_input("Number 1")
number2 = st.number_input("Number 2")
number3 = st.number_input("Number 3")

st.subheader('Result')
if number1 > number2 and number1 > number3:
      st.write('Number 1 is the largest')
else if  number2 > number1 and number2 > number3:
     st.write('Number 2 is the largest')
else if  number3 > number1 and number3 > number2:
     st.write('Number 3 is the largest')

