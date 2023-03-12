import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np
from io import StringIO



add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


form = st.form(key='my-form')
name = form.text_input('Enter Your Name')
age = form.number_input('Enter Your Age')
classd = form.text_input('Enter Your Class')
submit = form.form_submit_button('submit')


st.write('Press submit to have your name printed below')

if submit:
	if name == 'Wonder':
		st.write('Hello Wonder')
	else:
		st.write(f'hello {name} you are {age} years old and you are in {classd} class')



tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10,1)

tab1.subheader("A tab with a chat")
tab1.line_chart(data)

tab2.subheader("A tab with Data")
tab2.write(data)

uploaded_file = st.file_uploader("Choose a file")
frm = st.form(key='my_form')
tec = frm.text_input('Enter the Name of the File to Upload')
sub = frm.form_submit_button('Submit')

if uploaded_file is not None:
    

    # To read file as string:


    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.subheader('DATA DISPLAY SECTION')
    
    df = st.dataframe(dataframe)

    print(dataframe)

    

