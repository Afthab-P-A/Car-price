import pandas as pd
import streamlit as st
import pickle

st.title('Car Price predictor')
model=pickle.load(open('car_price_pred.sav','rb'))
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{"https://th.bing.com/th/id/OIP.o-QaHOIqb9DfiNgi5W3ntwHaE8?rs=1&pid=ImgDetMain"}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("https://th.bing.com/th/id/OIP.o-QaHOIqb9DfiNgi5W3ntwHaE8?rs=1&pid=ImgDetMain")

#['Location', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission','Owner_Type',
# 'Mileage', 'Engine', 'Power', 'Seats', 'Brand']
brands=['Maruti', 'Hyundai', 'Honda', 'Audi', 'Nissan', 'Toyota',
       'Volkswagen', 'Tata', 'Land', 'Mitsubishi', 'Renault',
       'Mercedes-Benz', 'BMW', 'Mahindra', 'Ford', 'Porsche', 'Datsun',
       'Jaguar', 'Volvo', 'Chevrolet', 'Skoda', 'Mini', 'Fiat', 'Jeep',
       'Smart', 'Ambassador', 'Isuzu', 'ISUZU', 'Force', 'Bentley',
       'Lamborghini']
loc=['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur',
      'Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']
years=[2010, 2015, 2011, 2012, 2013, 2016, 2018, 2014, 2017, 2007, 2009,
       2008, 2019, 2006, 2005, 2004, 2002, 2000, 2003, 1999, 2001, 1998]
ftypes=['CNG', 'Diesel', 'Petrol', 'LPG', 'Electric']

brand=st.selectbox("Brand",sorted(brands))

col1,col2,col3=st.columns(3)
with col1:
    location=st.selectbox('Location',sorted(loc))
with col2:
    year=st.selectbox('Year',sorted(years,reverse=True))
with col3:
    km=st.number_input('KM Driven')

col1,col2,col3=st.columns(3)
with col1:
    f_type=st.selectbox('Fuel Type',sorted(ftypes))
with col2:
    T_type=st.selectbox('Transmission Type',['Manual', 'Automatic'])
with col3:
    O_type=st.selectbox('Ownership',['First', 'Second','Third', 'Fourth & Above'])

col1,col2,col3,col4=st.columns(4)
with col1:
    mil=st.number_input('Mileage/Littre',min_value=1,max_value=30)
with col2:
    cc=st.number_input('Engine in CC',min_value=500)
with col3:
    power=st.number_input('Power in BHP',min_value=20)
with col4:
    seats=st.number_input('No.of seats',min_value=2,max_value=10)

if st.button('Expected Price Of Car'):

    df=pd.DataFrame({'Location':[location],
                     'Year':[year],
                     'Kilometers_Driven':[km],
                     'Fuel_Type':[f_type],
                     'Transmission':[T_type],
                     'Owner_Type':[O_type],
                     'Mileage':[mil],
                     'Engine':[cc],
                     'Power':[power],
                     'Seats':[seats],
                     'Brand':[brand]})
    result=model.predict(df)
    price=round(result[0],2)
    st.text(f"Expected Price of car is {price} Lakhs")

