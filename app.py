import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                         BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]

            # Validate input ranges
            if not (0 <= user_input[0] <= 20 and  # Pregnancies
                    70 <= user_input[1] <= 200 and  # Glucose
                    60 <= user_input[2] <= 140 and  # BloodPressure
                    0 <= user_input[3] <= 100 and  # SkinThickness
                    0 <= user_input[4] <= 846 and  # Insulin
                    18.5 <= user_input[5] <= 70 and  # BMI
                    0 <= user_input[6] <= 2.5 and  # DiabetesPedigreeFunction
                    0 <= user_input[7] <= 120):  # Age
                diab_diagnosis = 'The data is Not matching'
            else:
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = 'The data is Not matching'

        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)')

    with col3:
        cp = st.text_input('Chest Pain types (0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-3)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            # Validate input ranges
            if not (20 <= user_input[0] <= 100 and  # age
                    user_input[1] in [0, 1] and  # sex
                    0 <= user_input[2] <= 3 and  # cp
                    90 <= user_input[3] <= 200 and  # trestbps
                    100 <= user_input[4] <= 600 and  # chol
                    user_input[5] in [0, 1] and  # fbs
                    0 <= user_input[6] <= 2 and  # restecg
                    60 <= user_input[7] <= 220 and  # thalach
                    user_input[8] in [0, 1] and  # exang
                    0 <= user_input[9] <= 6.2 and  # oldpeak
                    0 <= user_input[10] <= 2 and  # slope
                    0 <= user_input[11] <= 3 and  # ca
                    0 <= user_input[12] <= 2):  # thal
                heart_diagnosis = 'The data is Not matching'
            else:
                heart_prediction = heart_disease_model.predict([user_input])
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'The data is Not matching'

        st.success(heart_diagnosis)
