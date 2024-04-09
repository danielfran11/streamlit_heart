# Importing essential libraries
import pickle
import streamlit
import streamlit as st

# Load the Random Forest CLassifier model
model = pickle.load(open('model.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Jantung')

col1, col2 = st.columns(2)

with col1:
    age = st.text_input ('Masukan usia (age)')
with col2:
    sex = st.text_input (' Masukan jenis kelamin (sex)')
with col1:
    cp = st.text_input ("Masukan tingkatan nyeri dada (cp)")
with col2:
    trestbps = st.text_input ('Masukan angka tekanan darah (trestbps)')
with col1:
    chol = st.text_input ('Masukan angka kolesterol (chol)')
with col2:
    fbs = st.text_input ('Masukan angka gula darah puasa (fbs)')
with col1:
    restecg = st.text_input ('Masukan angka resting electrocardiographic (restecg)')
with col2:
    thalach = st.text_input ('Masukan angka detak jantung maksimum (thalach)')
with col1:
    exang = st.text_input ('Masukan angka exercise induced angina (exang)')
with col2:
    oldpeak = st.text_input ('Masukan angka depression induced (oldpeak)')
with col1:
    slope = st.text_input ('Masukan angka kemiringan segmen latihan ST (slope)')
with col2:
    ca = st.text_input ('Masukan angka major vessels (ca)')
with col1:
    thal = st.text_input ('Masukan angka tipe jenis defek jantung (thal)')


heart_diagnose = ' '

if st.button('Prediksi penyakit jantung') :
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if(heart_prediction[0] == 1):
        heart_diagnose = 'Pasien terkena penyakit jantung'
    else:
        heart_diagnose = 'Pasien tidak terkena penyakit jantung'

    st.write("Hasil Prediksi: ")
    st.write(heart_diagnose)