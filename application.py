import numpy as np
import matplotlib as plt
import streamlit as st 
import pandas as pd
import seaborn as sns

#1.Title and Subheader

st.title("Data Analysis")
st.subheader("Data Analysis using Python & Streamlit")

#2.Upload Dataset

upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)
    
#3. Show Dataset

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
#4.Check Datatype of Each Column  

if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)   
        
#5. Find Shape of Dataset (Number of rows and columns) 

if upload is not None:
    data_shape = st.radio("What Dimension do you want to check?",('Rows','Columns'))
    
    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == "Columns":
        st.text("Number of columns")
        st.write(data.shape[1])
        
#6. Find Null Values in the Dataset

if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!, No Missing Values")

#7. Find Duplicate Values in the Dataset

if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset contains some duplicated values")
        dup = st.selectbox("Do you want to remove duplicated values?", \
                           ("Select One","Yes","No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicated Values are removed")
        if dup == "No":
            st.text("Ok No Problem!")  
            
#8. Get Overall Statistics

if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include="all")) 

#9. Information of Dataset

if upload is not None:
    if st.checkbox("Information of the Dataset"):
        st.write(data.info)        
        
#10. About Section

if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks To streamlit")
    
if st.checkbox("By"):
    st.success("Dhruvil Shah")
            

        