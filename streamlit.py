import streamlit as st
import pandas as pd
import numpy as np


#Title of the application 
st.title("Hello World")

##Display text
st.write('this is a simple text')



#Creating a dataframe
dataFrame = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20,30,40]
})


#to display the dataframe
st.write('This is the dataframe')
st.write(dataFrame)


#creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)