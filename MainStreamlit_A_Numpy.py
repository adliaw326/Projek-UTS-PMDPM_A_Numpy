import streamlit as st
import pickle
import os

from streamlit_option_menu import option_menu

model_path_clf = 'BestModel_CLF_RandomForest_Numpy.pkl'
model_path_reg = 'BestModel_REG_LassoRegression_Numpy.pkl'

with open(model_path_clf, 'rb') as f:
    loaded_model_clf = pickle.load(f)

with open(model_path_reg, 'rb') as f:
    loaded_model_reg = pickle.load(f)

rf_model = loaded_model_clf
lasso_model = loaded_model_reg

with st.sidebar:
    selected = option_menu('Tutorial Desain Streamlit UTS ML 24/25',
                           ['Klasifikasi', 'Regresi'],
                           default_index=0)

if selected == 'Klasifikasi':
    st.title('Klasifikasi')
    st.write('KLASIFIKASI MENGGUNAKAN ALGORITMA RANDOM FOREST CLASSIFICATION')
    squaremeters = st.number_input("Input Squaremeters", min_value=1, step=1)
    numberofrooms = st.number_input("Input Number of Rooms", min_value=1, step=1)    
    hasyard = st.selectbox("Has Yard?", ["Yes", "No"])
    haspool = st.selectbox("Has Pool?", ["Yes", "No"])
    floors = st.number_input("Jumlah Floor", min_value=1, step=1)
    citycode = st.number_input("Input City Code", min_value=1, step=1)
    citypartrange = st.slider("Input City Part Range", 1, 20, step=1)
    numprevowners = st.slider("Input Total Previous Owner", 1, 20, step=1)
    made = st.number_input("Made ", min_value=1, step=1)
    isnewbuilt = st.selectbox("Is New Built?", ["Yes", "No"])
    hasstormprotector = st.selectbox("Has Storm Protector?", ["Yes", "No"])
    basement = st.number_input("Input Luas Basement", min_value=1, step=1)
    attic = st.number_input("Input Luas Attic", min_value=1, step=1)
    garage = st.number_input("Input Luas Garage", min_value=1, step=1)
    hasstorageroom = st.selectbox("Has Storage Room?", ["Yes", "No"])
    hasguestroom = st.slider("Input Jumlah Guest Room", 1, 20, step=1)

    if hasyard=='Yes':
        hasyardY = 1
        hasyardN = 0
    elif hasyard == 'No':
        hasyardY = 0
        hasyardN = 1

    if haspool=='Yes':
        haspoolY = 1
        haspoolN = 0
    elif haspool == 'No':
        haspoolY = 0
        haspoolN = 1

    if isnewbuilt=='Yes':
        isnewbuiltY = 1
        isnewbuiltN = 0
    elif isnewbuilt == 'No':
        isnewbuiltY = 0
        isnewbuiltN = 1

    if hasstormprotector=='Yes':
        hasstormprotectorY = 1
        hasstormprotectorN = 0
    elif hasstormprotector == 'No':
        hasstormprotectorY = 0
        hasstormprotectorN = 1

    if hasstorageroom=='Yes':
        hasstorageroomY = 1
        hasstorageroomN = 0
    elif hasstorageroom == 'No':
        hasstorageroomY = 0
        hasstorageroomN = 1

    input_data=[[squaremeters, numberofrooms, hasyardY, hasyardN, haspoolY, haspoolN,
                floors, citycode, citypartrange, numprevowners,
                made, isnewbuiltY, isnewbuiltN, hasstormprotectorY, hasstormprotectorN, basement,
                attic, garage, hasstorageroomY, hasstorageroomN, hasguestroom]]

    st.write("Data rumah yang akan diinput ke model")
    st.write(input_data)

    if st.button("Prediksi"):
        hasil = rf_model.predict(input_data)
        outcome_names = {'Basic': 'Basic', 'Middle': 'Middle', 'Luxury': 'Luxury'}
        st.write(f"Rumah tersebut diprediksi termasuk ke dalam kategori **{outcome_names[hasil[0]]}** oleh Random Forest")



if selected =='Regresi':
    st.title('Regresi')
    st.write('REGRESI MENGGUNAKAN ALGORITMA LASSO REGRESSION')
    squaremeters = st.number_input("Input Squaremeters", min_value=1, step=1)
    numberofrooms = st.number_input("Input Number of Rooms", min_value=1, step=1)    
    hasyard = st.selectbox("Has Yard?", ["Yes", "No"])
    haspool = st.selectbox("Has Pool?", ["Yes", "No"])
    floors = st.number_input("Jumlah Floor", min_value=1, step=1)
    citycode = st.number_input("Input City Code", min_value=1, step=1)
    citypartrange = st.slider("Input City Part Range", 1, 20, step=1)
    numprevowners = st.slider("Input Total Previous Owner", 1, 20, step=1)
    made = st.number_input("Made ", min_value=1, step=1)
    isnewbuilt = st.selectbox("Is New Built?", ["Yes", "No"])
    hasstormprotector = st.selectbox("Has Storm Protector?", ["Yes", "No"])
    basement = st.number_input("Input Luas Basement", min_value=1, step=1)
    attic = st.number_input("Input Luas Attic", min_value=1, step=1)
    garage = st.number_input("Input Luas Garage", min_value=1, step=1)
    hasstorageroom = st.selectbox("Has Storage Room?", ["Yes", "No"])
    hasguestroom = st.slider("Input Jumlah Guest Room", 1, 20, step=1)

    if hasyard=='Yes':
        hasyardY = 1
        hasyardN = 0
    elif hasyard == 'No':
        hasyardY = 0
        hasyardN = 1

    if haspool=='Yes':
        haspoolY = 1
        haspoolN = 0
    elif haspool == 'No':
        haspoolY = 0
        haspoolN = 1

    if isnewbuilt=='Yes':
        isnewbuiltY = 1
        isnewbuiltN = 0
    elif isnewbuilt == 'No':
        isnewbuiltY = 0
        isnewbuiltN = 1

    if hasstormprotector=='Yes':
        hasstormprotectorY = 1
        hasstormprotectorN = 0
    elif hasstormprotector == 'No':
        hasstormprotectorY = 0
        hasstormprotectorN = 1

    if hasstorageroom=='Yes':
        hasstorageroomY = 1
        hasstorageroomN = 0
    elif hasstorageroom == 'No':
        hasstorageroomY = 0
        hasstorageroomN = 1

    input_data=[[squaremeters, numberofrooms, hasyardY, hasyardN, haspoolY, haspoolN,
                floors, citycode, citypartrange, numprevowners,
                made, isnewbuiltY, isnewbuiltN, hasstormprotectorY, hasstormprotectorN, basement,
                attic, garage, hasstorageroomY, hasstorageroomN, hasguestroom]]

    st.write("Data rumah yang akan diinput ke model")
    st.write(input_data)

    if st.button("Prediksi"):
        hasil=lasso_model.predict(input_data)
        st.markdown(f"Prediksi Harga Rumah yang telah diinputkan adalah: Rp {hasil[0]:,.2f} oleh Lasso Regression")
