# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:49:20 2023

@author: dc
"""

import pandas as pd
import streamlit as st
import joblib

def main():
    
    html_temp ="""
    <div style="background-color:lightblue;padding:15px 100px;margin:60px 10">
    <h2 style="color:black";text-align:center;> Loan Status Prediction Using ML </h2>
    </div>
    
    
    """
    
  
    
    st.markdown(html_temp , unsafe_allow_html=True)
    
    model = joblib.load('D:\Machine Learning\Interface Project\project 2 Loan Status\loan_status_predict')
    name = st.text_input('Enter your Name')
    
    s1 = st.selectbox('Gender', ('Male','Female'))
    
    if s1=='Male':
        p1 = 1
    else:
        p1 = 0

    
    
    s2 = st.selectbox('Married', ('Yes','No'))
    
    if s2=='Yes':
        p2= 1
    else:
        p2=0
    
    p3 = float(st.selectbox("Dependents",(0,1,2,4) ))
    
    
    
    s4 = st.selectbox('Education', ('Graduate','Not Graduate'))
    
    if s4=='Not Graduate':
        p4 = 0
    else:
        p4 = 1
        
    s5=st.selectbox('Self Employed',('Yes','No'))
       
    if s5=="Yes":
        p5 = 1
    else:
        p5 = 0
        
    
   
    p6 = st.number_input("Enter Applicant Income")
    
    p7 = st.number_input("Enter Coapplicant Income ")

    
    p8 = st.number_input("Enter Loan Amount")
    
    p9 = st.number_input("Enter Loan Amount Term")
    
    s10 = st.selectbox('Credit History',('Yes','No'))
    
    if s10=='Yes':
        p10 = 1
    else:
        p10 = 0
        
        
    s11=st.selectbox('Select Property Area',('Rural','Ubran','Semiurban'))
    
    if s11=='Rural':
        p11 = 0
    elif s11 == 'Ubran':
        p11 = 1
    else:
        p11 = 2
    
    
    result = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]])

    if st.button('Predict'):
        print(result)

        if result[0] == 1:
            st.balloons()
            st.success('>&#x2705; The Loan Is Approved ')
            #st.error('&#x274C; The Loan Is Not Approved ')

        else:
            #st.markdown("<span style='color:red;font-size:24px;'>&#x274C;</span>", unsafe_allow_html=True)

            st.error('&#x274C; The Loan Is Not Approved ')
            #st.markdown("<span style='color:red;font-size:24px;'>&#x274C;</span> The Loan Is Not Approved.", unsafe_allow_html=True)

        
    
    
    

    
    
    
    
    
    
main()