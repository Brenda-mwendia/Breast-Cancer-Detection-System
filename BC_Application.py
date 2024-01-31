import os
import numpy as np
from keras.models import load_model
import streamlit as st
import cv2 as cv
from PIL import Image
import csv
import pandas as pd


def create_csv(file_name, header):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)


def append_csv(file_name, data):
    with open(file_name, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)


file_name = 'patient_data.csv'
header = ['Patient Name', 'Gender', 'ID', 'Diagnosis']


if not os.path.isfile(file_name):
    create_csv(file_name, header)

def home_page():
    categories = ['Benign Breast Cancer', 'Malignant Breast Cancer']
    st.title('Breast Cancer Detection And Diagnosis Application')
    patient_name = st.text_input('Enter Patient Name:')
    patient_gender = st.selectbox('Enter Patient Gender:', options=['Male', 'Female'])
    patient_id = st.text_input('Enter Patient ID:')
    st.text('upload the image')

    uploaded_file = st.file_uploader('Choose an image...')

    model = load_model('C:/Users/admin/Desktop/BREAST CANCER DETECTION SYSTEM/BC2/BCmodel.h5')

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='uploaded image')

        if st.button('DETECT'):
            st.write('result...')
            image = np.array(image)
            image = cv.resize(image, (50, 50))
            image = np.expand_dims(image/255, axis=0)

            result = model.predict(image)
            result = np.argmax(result)
            result = int(result)
            prediction = categories[result]
            st.title('Patient has: ')
            st.title(prediction)
            if result == 0:
                st.write('Benign breast cancer conditions are non-cancerous growths or changes in breast tissue. These are not classified as breast cancer.')
                st.title('Symptoms')
                st.write('Symptoms include:')
                st.write('1. Breast lumps or nodules: These may feel like solid masses or cysts filled with fluid.')
                st.write('2. Breast pain or tenderness: Many women with fibrocysts experience breast discomfort, especially during menstrual cycle.')
                st.write('3. Breast swelling or enlargement: Some conditions can lead to breast swelling')
                st.write('4. Nipple discharge: This can be clear, bloody or other colors and may occur spontaneously.')
                st.write('5. Skin changes: In some cases, the skin over the affected area may become dimpled or puckered.')
                st.title('Prevention Methods')
                st.write('Prevention methods include:')
                st.write('1. Regular breast self-exams: Perform monthly breast self-exams to become familiar with your breast tissue.')
                st.write('2. Maintain a healthy lifestyle: Eating a balanced diet, engaging in regular pysical activity and avoiding excessive alcohol consumption.')
                st.write('3. Hormone therapy: Discuss with your healthcare provider risks and benefits of hormone replacement therapy.')
                st.write('4. Manage stress: High stress levels may exacerbate some benign breast conditions.')
                st.write('5. Regular check-ups: Visit your healthcare provider for regular check-upsb and mammograms as recommended based on your age and risk factors.')
                st.title('Treatment Methods')
                st.write('1. Observation: Healthcare providers may recommend simply monitoring the condition.')
                st.write('2. Medications: Depending on the condition and symptoms, doctors may prescribe medications to allevaite pain or reduce inflammation.')
                st.write('3. Aspiration: If you have a breats cyst, your doctor may use needles to drain the cyst.')
                st.write('4. Surgery: In some cases, surgical removal of the tissues or lump may be necessary.')
                st.write('5. Hormone thrapy: Doctor may recommend hormonal therapy to manage symptoms.')
                st.write('6. Lifastyle changes: Making changes in your lifastyle such as reducing caffaine intake may help alleviate symptoms.')
            elif result ==1:
                st.write('Malignant breast cancer, often referred to simply as breast cancer, is a type of cancer that originates in the cells of the breast. It is characterized by the uncontrolled growth and division of abnormal cells in the breast tissue. These cancerous cells can invade nearby tissue and may also spread to other parts of the body through the lymphatic system or bloodstream')
                st.title('Symptoms')
                st.write('1. A lump in the breast: This is one the common and noticable signs of breast cancer.')
                st.write('2. Changes in breast size, shape or appearance: This may include swelling, dimpling or puckering of the breast skin')
                st.write('3. Nipple changes: Look for the changes in nipple, such as inversion redness, scaling or discharge')
                st.write('4. Breast pain: Although not always a symptom, some people with breast cancer may experience breast pain or discomfort.')
                st.write('5. Skin changes: Changes in the skin on or around the breast, like redness or peeling can be a sign or rare but aggressive form of breast cancer.')
                st.write('6. Unexpected weight loss: Sudden, unexplained weight loss can be a symptom of advanced breast cancer.')
                st.title('Prevention methods')
                st.write('1. Regular Breast Self-Exams: Perform monthly breast self-exams to become familiar with your breast tissue.')
                st.write('2. Healthy Lifestyle Choices: Maintain a healthy lifestyle by eating a balanced diet, engaging in regular physical activity and limiting alcohol consumption.')
                st.write('3. Breastfeeding: If you have the opportunity, breastfeeding can lower the risk of breast cancer.')
                st.write('4. Limit hormone therapy: If you are considering hormone replacement therapy, discuss risks and benefits with your healthcare provider.')
                st.write('5. Screening and early detection: Follow recommended screening guidelines, including regular mammograns and clinical breast exams.')
                st.write('6. Know your family history: Be aware of your family medical history.')
                st.write('7. Consider Risk-Reducing Medications or Surgeries: In some cases, individuals at high risks for breast cancer my discuss risk-reducing medication or preventive surgeries.')
                st.title('Treatment methods')
                st.write('1. Surgery: Surgery is often the prinary treatment for breast cancer.')
                st.write('2. Radiation therapy: Radiation therapy uses high X-rays to target and destroy cancer cells.')
                st.write('3. Chemotherapy: Chemotherapy involves the use of drugs to kill cancer cells or stop their growth.')
                st.write('4. Hormone Therapy: For hormone receptor-positive breast cancers, hormone therapy drugs can be used to block the effects of hormones that promote cancer growths.')
                st.write('5. Targeted Therapy: Targeted therapy are medications that specifically target cancer cells with certain characteristics.')
                st.write('6. Immunotherapy: In some cases, immunotherapy may be used to boost the bodys immune system to fight breast cancer')
                st.write('7. Clinical trials: Participation in clinical trials can provide access to innovative treatments and therapies that are still under investigation.')
                st.write('8. Breast Reconstruction: After mastectomy, some individuals choose breats cancer reconstruction surgery to restore the breasts appearance.')
            
            
            data = [patient_name, patient_gender, patient_id, prediction]

            append_csv(file_name, data)



def search_page():
    st.title('Search Patient Data')
    

    df = pd.read_csv('patient_data.csv')

    search_method = st.selectbox('Search by: ', ('Name', 'Cancer Type'))

    def search_by_name():
        name = st.text_input('Enter name of patient:')
        if st.button('SEARCH'):
            filtered = df[(df['Patient Name'] == name)]
            if name in filtered['Patient Name'].unique():
                st.dataframe(filtered)
            else:
                st.title('No such patient found')

    def search_by_cancer_type():
        type = st.selectbox('Select Cancer Type:', ('Benign Breast Cancer', 'Malignant Breast Cancer'))
        if st.button('SEARCH'):
            filtered = df[(df['Diagnosis'] == type)]
            st.dataframe(filtered)


    if search_method == 'Name':
        search_by_name()
    else:
        search_by_cancer_type()



page_options = ['Home Page', 'Search Page']

selected_page = st.sidebar.selectbox('Navigate to:', page_options)


if selected_page == 'Home Page':
    home_page()
else:
    search_page()