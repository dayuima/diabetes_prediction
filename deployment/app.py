import streamlit as st
import pandas as pd
import numpy as np
import joblib

with open('rfc_model.pkl','rb') as file_1:
  rfc_model = joblib.load(file_1)


st.title("Diabetes Disease Prediction")

st.subheader(" Ayo Periksa Kesehatan Anda !! ")

Name = st.text_input("Nama :")

Pregnancies = st.slider('Jumlah kehamilan :', min_value = 0, max_value = 17, value = 3)
st.write(Pregnancies)

Glucose = st.number_input('Konsentrasi glukosa dalam darah (mg/dL) :', min_value = 44, max_value = 199, value = 44)
st.write(Glucose)

BloodPressure = st.number_input('Tekanan darah (mm/Hg) :', min_value = 24, max_value = 122, value = 24)
st.write(BloodPressure)

SkinThickness = st.slider('Ketebalan lipatan kulit trisep (mm) :', min_value = 7, max_value = 99, value = 25)
st.write(SkinThickness)

Insulin = st.number_input('Kadar insulin dalam darah (μU/mL) :', min_value = 14, max_value = 846, value = 14)
st.write(Insulin)

BMI = st.number_input('Indeks massa tubuh (kg/m^2) :', min_value = 18.2, max_value = 67.1, value = 18.2)
st.write(BMI)

DiabetesPedigreeFunction = st.number_input('Riwayat diabetes dalam keluarga :', min_value = 0.078, max_value = 2.42, value = 0.078)
st.write(DiabetesPedigreeFunction)

Age = st.slider('Usia :', min_value = 21, max_value = 81, value = 25)
st.write(Age)


df_inf = pd.DataFrame({
    'pregnancies':[Pregnancies],
    'glucose':[Glucose],
    'bloodpressure':[BloodPressure],
    'skinthickness':[SkinThickness],
    'insulin':[Insulin],
    'bmi':[BMI],
    'diabetespedigreefunction':[DiabetesPedigreeFunction],
    'age':[Age]
})

model_rfc1 = rfc_model.predict(df_inf[['pregnancies','glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']])

if st.button('Predict'): 
    final_result_rfc = rfc_model.predict(df_inf[['pregnancies','glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']])
    st.write('Hasil Prediksi: ')
    if final_result_rfc == 1:
        st.subheader('Kami sangat menyesal mengatakan bahwa sepertinya Anda menderita diabetes')
    else:
        st.subheader('Selamat Anda tidak menderita Diabetes')

st.write('Terima kasih telah menggunakan aplikasi ini untuk memeriksa kesehatan Anda. Jangan lupa untuk selalu memperhatikan kesehatan Anda dengan menerapkan pola hidup sehat dan teratur melakukan pemeriksaan kesehatan secara berkala.')

