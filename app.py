import streamlit as st

st.write("""
# Find the largest

This app find the largest number among three numbers
""")
#Get Input

st.header('Input Parameters')

def user_input_features():
    number1 = st.number_input("Number_1")
    number2 = st.number_input("Number_2")
    number3 = st.number_input("Number_3")
   
    data = {'Number_1': number1,
           'Number_2': number2,
            'Number_3': number3,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Prediction')
if df['Number_1'] == 10:
    st.write('Approved')
else:
    st.write('Declined')

