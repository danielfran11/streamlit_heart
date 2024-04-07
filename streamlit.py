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
thalach = st.text_input ('Masukan angka detak jantung maksimum (thalach)')

heart_diagnose = ' '

if st.button('Prediksi penyakit jantung') :
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, thalach]])

    if(heart_prediction[0] == 1):
        heart_diagnose = 'Pasien terkena penyakit jantung'
    else:
        heart_diagnose = 'Pasien tidak terkena penyakit jantung'

    st.success(heart_diagnose)
    