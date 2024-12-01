# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:47:58 2024

@author: Jhanavi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loding saved model

diabetes_model = pickle.load(open('C:/Users/Jhanavi/Downloads/Multiple Disease Prediction System/saved model/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/Jhanavi/Downloads/Multiple Disease Prediction System/saved model/heart_model.sav', 'rb'))

#sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Diseaes Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['activity', 'heart'],
                           default_index=0)
    
# diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction Using AI/ML')
    
    # getting input data from the user
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        Pregnancies = st.text_input('Number Of Pregnancies')   
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
       SkinThickness = st.text_input('Skin thickness value')
    with col2:
      Insulin = st.text_input('Insulin Level')  
    with col3:
      BMI = st.text_input('BMI Level') #body mass index values  
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Predigree function value') 
    with col2:
      Age = st.text_input('Age of the person') 
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        
       try:
            # Convert input data to appropriate types
            input_data = [
                float(Pregnancies.strip()),
                float(Glucose.strip()),
                float(BloodPressure.strip()),
                float(SkinThickness.strip()),
                float(Insulin.strip()),
                float(BMI.strip()),
                float(DiabetesPedigreeFunction.strip()),
                float(Age.strip())
            ]
            
            # Make prediction
            diab_prediction = diabetes_model.predict([input_data])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            
            st.success(diab_diagnosis)
        
       except ValueError:
            st.error("Please enter valid numeric values for all fields.")    
    
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Using AI/ML')
    
    # getting input data from the user
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        age = st.text_input('Age')   
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest pain types')
    
    with col1:
       trestbps = st.text_input('Resting blood pressure')
    with col2:
      chol = st.text_input('Serum cholestoral in mg/dl')  
    with col3:
      fbs = st.text_input('Fasting Blood sugur > 120 mg/dl') #body mass index values  
    with col1:
       restecg = st.text_input('Resting Electrocardiographic results') 
    with col2:
      thalach = st.text_input('maximum heart rate achieved')
    with col3:
        exang = st.text_input('exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col1:
        slope = st.text_input('the slope of the peak exercise ST segment')
    with col2:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    #code for prediction
    heart_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        try:
           # Convert input data to appropriate types
           input_data = [
               float(age.strip()),
               float(sex.strip()),
               float(cp.strip()),
               float(trestbps.strip()),
               float(chol.strip()),
               float(fbs.strip()),
               float(restecg.strip()),
               float(thalach.strip()),
               float(exang.strip()),
               float(oldpeak.strip()),
               float(slope.strip()),
               float(ca.strip()),
               float(thal.strip())
           ]
           
           # Make prediction
           heart_prediction = heart_model.predict([input_data])
           if heart_prediction[0] == 1:
               heart_diagnosis = 'The person has heart disease'
           else:
               heart_diagnosis = 'The person does not have heart disease'
           
           st.success(heart_diagnosis)
       
        except ValueError:
           st.error("Please enter valid numeric values for all fields.")
        
     
    
    