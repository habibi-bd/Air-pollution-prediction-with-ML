import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings("ignore")
import streamlit as st


model="final_model.pkl"
scaler= "scaler.pkl"
label_encoder = "label_encoder.pkl"

loaded_model = pickle.load(open(model, 'rb'))
loaded_scaler = pickle.load(open(scaler, 'rb'))
loaded_label_encoder = pickle.load(open(label_encoder, 'rb'))



new_user_data = pd.DataFrame({
    'Temperature': [25.5],
    'Humidity': [60.0],
    'PM2.5': [15.0],
    'PM10': [30.0],
    'NO2': [10.0],
    'SO2': [5.0],
    'CO': [2.0],
    'Proximity_to_Industrial_Areas': [0.1],
    'Population_Density': [1500]
})



user_data_scaled = loaded_scaler.transform(new_user_data)


# Predict the air quality
predicted_air_quality_encoded = loaded_model.predict(user_data_scaled)

# Inverse transform the predicted value to get the original label
predicted_air_quality_label = loaded_label_encoder.inverse_transform(predicted_air_quality_encoded)

# print("Predicted Air Quality for the new user:", predicted_air_quality_label[0])

# -------------------------------------------STREAMLIT-------------------------------------------------------------------------

color_map = {
    'Good': 'green',
    'Moderate': 'orange',
    'Poor': 'red',
    'Hazardous': 'darkred'
}
st.title("🌍 Air Quality Prediction App")


st.header("Enter Environmental Parameters")
temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.5)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
pm25 = st.slider("PM2.5 (µg/m³)", 0.0, 500.0, 15.0)
pm10 = st.slider("PM10 (µg/m³)", 0.0, 500.0, 30.0)
no2 = st.slider("NO2 (ppb)", 0.0, 200.0, 10.0)
so2 = st.slider("SO2 (ppb)", 0.0, 200.0, 5.0)
co = st.slider("CO (ppm)", 0.0, 50.0, 2.0)
proximity = st.slider("Proximity to Industrial Areas (0-1)", 0.0, 1.0, 0.1)
population_density = st.number_input("Population Density (people/km²)", min_value=0, value=1500)

user_data = pd.DataFrame([{
    'Temperature': temperature,
    'Humidity': humidity,
    'PM2.5': pm25,
    'PM10': pm10,
    'NO2': no2,
    'SO2': so2,
    'CO': co,
    'Proximity_to_Industrial_Areas': proximity,
    'Population_Density': population_density
}])

if st.button("Predict Air Quality"):
    scaled_data = loaded_scaler.transform(user_data)
    prediction_encoded = loaded_model.predict(scaled_data)
    prediction_label = loaded_label_encoder.inverse_transform(prediction_encoded)[0]
    color = color_map.get(prediction_label, 'gray')

    # Display result with color
    st.markdown(
        f"<h2 style='color:{color};'>Predicted Air Quality: {prediction_label}</h2>",
        unsafe_allow_html=True
    )