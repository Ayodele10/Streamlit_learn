import streamlit as st
import pandas as pd


st.title("Streamlit text Input Widget Example")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")
    


#using a slider
age = st.slider('Select your age:',0,100,50)
st.write(f"Your age is {age}")



#select box
option = st.selectbox('Select your favorite color:',
                       ['Red', 'Green', 'Blue', 'Yellow']
                       )
st.write(f'Your favorite color is {option}')



#Creating a dataframe
data = pd.DataFrame({
    "Name": ["John", "Jane", "jaay", "hlal"],
    "Age": [23,323,34,33],
    "City": ['Laso', 'adfa', 'asdf','jalk']
})

st.write("Here is a sample dataframe:")
st.dataframe(data)
 

#Uploading a file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV file:")
    st.dataframe(df) 
   