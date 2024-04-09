# Importing essential libraries
import pickle
import streamlit
import streamlit as st

# Load the Random Forest CLassifier model
model = pickle.load(open('model.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Jantung')

age = st.text_input ('Masukan usia (age)')
sex = st.text_input (' Masukan jenis kelamin (sex)')
cp = st.text_input ("Masukan tingkatan nyeri dada (cp)")
trestbps = st.text_input ('Masukan angka tekanan darah (trestbps)')
chol = st.text_input ('Masuka angka kolesterol (chol)')
fbs = st.text_input ('Masukan angka gula darah puasa (fbs)')
restecg = st.text_input ('Masukan angka resting electrocardiographic (restecg)')
thalach = st.text_input ('Masukan angka detak jantung maksimum (thalach)')
exang = st.text_input ('Masukan angka exercise induced angina (exang)')
oldpeak = st.text_input ('Masukan angka depression induced (oldpeak)')
slope = st.text_input ('Masukan angka kemiringan segmen latihan ST (slope)')
ca = st.text_input ('Masukan angka major vessels (ca)')
thal = st.text_input ('Masukan angka tipe jenis defek jantung (thal)')


heart_diagnose = ' '

if st.button('Submit') :
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, thalach]])

    if(heart_prediction[0] == 1):
        heart_diagnose = 'Pasien terkena penyakit jantung'
    else:
        heart_diagnose = 'Pasien tidak terkena penyakit jantung'

    st.write("Hasil Prediksi: ")
    st.write(heart_diagnose)
    
