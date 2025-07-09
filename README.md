# Air-pollution-prediction-with-ML
In this project i included air pollution predict with machine learning algorithm and little bit streamlit for visualization
🌍 Air Quality Prediction App
This project is a machine learning-based web application that predicts air quality levels based on environmental parameters using a trained model. It is built with Streamlit for interactivity and visualization.

📸 Demo

🔍 Features
✅ Predict air quality levels using:

Temperature, Humidity

PM2.5, PM10

NO₂, SO₂, CO

Proximity to industrial areas

Population density

✅ Visualize predictions with color-coded labels:

🟢 Good

🟠 Moderate

🔴 Poor

🔴 Hazardous

✅ Built with:

scikit-learn for model training

StandardScaler for input normalization

LabelEncoder for class mapping

Streamlit for the web interface

🛠 Technologies Used
Technology	Purpose
Python	Programming language
Pandas	Data handling
Scikit-learn	Machine learning + preprocessing
Pickle	Model & encoder serialization


Streamlit	Front-end UI for prediction

🚀 Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/air-quality-predictor.git
cd air-quality-predictor
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

txt
Copy
Edit
streamlit
pandas
scikit-learn
Run the App

bash
Copy
Edit
streamlit run app.py
🧠 How It Works
During training:

A machine learning model is trained on labeled air quality data.

A StandardScaler is used to normalize inputs.

A LabelEncoder maps air quality categories to numeric values.

All components are saved using pickle.

During inference:

User inputs are collected via Streamlit sliders.

Inputs are scaled using the same scaler used during training.

The model predicts an encoded air quality class.

The label is decoded back into a readable format (e.g., “Good”).

📂 Project Structure
bash
Copy
Edit
air-quality-predictor/
│
├── app.py                  # Streamlit app
├── final_model.pkl         # Trained ML model
├── scaler.pkl              # StandardScaler object
├── label_encoder.pkl       # LabelEncoder object
├── requirements.txt        # Python dependencies
└── README.md               # Project info
📊 Example Input & Output
Input:

Temperature: 25.5 °C

Humidity: 60%

PM2.5: 15 µg/m³

CO: 2 ppm
...

Output:

yaml
Copy
Edit
Predicted Air Quality: Good ✅
🧪 To Improve This Project
Use imbalanced-learn to fix class imbalance

Add charts (e.g., pie chart of class probabilities)

Deploy using Streamlit Cloud, Render, or Hugging Face Spaces

👤 Author
Adnan Habib
🧠 Student | 💻 Data Science Enthusiast
Feel free to connect and star ⭐ the project if it helped you!

📜 License
This project is licensed under the MIT License.
You are free to use, share, and modify with attribution.
