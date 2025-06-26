# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:48:17 2025

@author: lokes
"""


from streamlit_option_menu import option_menu
import streamlit as st
import pickle



diabetes_model = pickle.load(open("C:/Users/lokes/Desktop/nan/saved diseases code/diabetes.sav",'rb'))

heart_disease_model = pickle.load(open("C:/Users/lokes/Desktop/nan/saved diseases code/heart.sav",'rb'))

parkinson_model = pickle.load(open("C:/Users/lokes/Desktop/nan/saved diseases code/parkinson.sav",'rb'))

with st.sidebar:
    selected = option_menu("MULTI DISEASE PREDICTION USING ML",
                           ['Diabetes Prediction','Heart disease Prediction','Parkinson Disease Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction")
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input("Number of Pregnancies")
        
    with col2:
        glucose = st.number_input("Glucose Value")
        
    with col3:
        BloodPressure = st.number_input("BloodPressure Level")
        
    with col1:
        SkinThickness = st.number_input("SkinThickness Level")
        
    with col2:
        insulin = st.number_input("Insulin Level")
    
    with col3:
        BMI = st.number_input("BMI value")
        
    with col1:
        DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction Value")
        
    with col2:
        Age = st.number_input("Age of Person")
        
    diagonsis = ''
    if st.button("Diabetes Test Result"):
        diabetes_pred = diabetes_model.predict([[pregnancies,glucose,BloodPressure,SkinThickness,insulin,BMI,DiabetesPedigreeFunction,Age]])
         
        if diabetes_pred[0]==0:
            diagonsis = 'The person is Non Diabetic'
        else:
            diagonsis = 'The person is Diabetic'
    st.success(diagonsis)
    
    
if selected == 'Heart disease Prediction':
    st.title("Heart Disease prediction")
    
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        age = st.number_input("Age of Person")
    
    with col2:
        sex = st.number_input("Gender")
        
    with col3:
        cp = st.number_input("Cp value")
    
    with col4:
        trestbps = st.number_input("Trestbps Value")
        
    with col1:
        chol = st.number_input("Chol Value")
    
    with col2:
        fbs = st.number_input("Fbs Value")
    
    with col3:
        restecg = st.number_input("restecg Value")
        
    with col4:
        thalach = st.number_input("Thalach value")
        
    with col1:
        exang = st.number_input("Exang Value")
        
    with col2:
        oldpeak = st.number_input("Oldpeak Value")
    
    with col3:
        slope = st.number_input("Scope")
        
    with col4:
        ca = st.number_input("CA")
        
    with col1:
        thal = st.number_input("Thal")
        
    heart_diag = ''
        
    if st.button("Heart Disease test results"):
        
        heart_d = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_d[0] ==0:
            heart_diag = 'The person have no heart Disease'
        else:
            heart_diag = 'The person have heart Disease'
    st.success(heart_diag)
    
if selected == 'Parkinson Disease Prediction':
    st.title("Parkinson's Disease Prediction")

    col1,col2,col3,col4,col5,col6 = st.columns(6)
    
    with col1:
        Fo = st.number_input("MDVP:Fo(Hz)")
        
    with col2:
        Fhi = st.number_input("MDVP:Fhi(Hz)")
        
        
    with col3:
        Flo = st.number_input("MDVP:Flo(Hz)")
        
    with col4:
       Jitte = st.number_input("MDVP:Jitter(%)")
        
    with col5:
       Jitter = st.number_input("MDVP:Jitter(Abs)")
    
    with col6:
        RAP = st.number_input("MDVP:RAP")
       
    with col1:
        PPQ = st.number_input("MDVP:PPQ")
        
    with col2:
        DDP = st.number_input("Jitter:DDP")
        
    with col3:
        Shimmer = st.number_input("Shimmer")
        
    with col4:
        shimmer_db = st.number_input("MDVP:Shimmer(dB)")
        
    with col5:
        shimmer_APQ3 = st.number_input("Shimmer:APQ3")
    
    with col6:
        shimmer_APQ5 = st.number_input("Shimmer:APQ5")
    
    with col1:
        APQ = st.number_input("MDVP:APQ")
        
    with col2:
        shimmer_DDA = st.number_input("Shimmer:DDA")
        
    with col3:
        NRH = st.number_input("NHR")
        
    with col4:
        HNR = st.number_input("HNR")
        
    with col5:
        RPDE = st.number_input("RPDE")
    
    with col6:
        DFA = st.number_input("DFA")
    
    with col1:
        spread_1 = st.number_input("spread1")
        
    with col2:
        spread_2 = st.number_input("spread2")
        
    with col3:
        D_2 = st.number_input("D2")
        
    with col4:
        PPE = st.number_input("PPE")
     
    
      
    
    park_diag = ''
    
    if st.button("Parkinson's Disease Test Results"):
        
        d = [[Fo,Fhi,Flo,Jitte,Jitter,RAP,PPQ,DDP,Shimmer,shimmer_db,shimmer_APQ3,shimmer_APQ5,APQ,shimmer_DDA,NRH,HNR,RPDE,DFA,spread_1,spread_2,D_2,PPE]]
        
        prediction = parkinson_model.predict(d)
        
        if prediction[0]==0:
            park_diag = "The person have no Parkinson's Disease"
            
        else:
            park_diag = "The person have Parkinson Disease"
            
    st.success(park_diag)
            
