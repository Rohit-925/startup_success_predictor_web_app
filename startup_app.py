
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:44:24 2023

@author: rohit
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("best_model.pkl","rb")
best_model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_startup_success(age_first_funding_year, age_last_funding_year, age_first_milestone_year, age_last_milestone_year):
    prediction =best_model.predict([[age_first_funding_year, age_last_funding_year, age_first_milestone_year, age_last_milestone_year]])
    print(prediction)
    return prediction
    
    
    
    


def main():
    st.title("Startup-Success-Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Startup-Success-Prediction ML App </h2>
     </div>
     <div>
    <h2 style="color:white;text-align:center;">Output: 1--Success , Output: 0-- Failure </h2>
    </div>
    """
    
   
    st.markdown(html_temp,unsafe_allow_html=True)
    age_first_funding_year = st.text_input("age_first_funding_year","Type Here")
    age_last_funding_year = st.text_input("age_last_funding_yearkewness","Type Here")
    age_first_milestone_year = st.text_input("age_first_milestone_year","Type Here")
    age_last_milestone_year = st.text_input("age_last_milestone_year","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_startup_success(age_first_funding_year, age_last_funding_year, age_first_milestone_year, age_last_milestone_year)
    st.success('The output is {}'.format(result))
   
        
    
      
        
        
if __name__=='__main__':
    main()

