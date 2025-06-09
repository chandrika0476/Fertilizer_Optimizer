from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Generate and train the model (this section is only for demonstration; ideally, model training should be separate)
soil_types = ['sandy', 'loamy', 'clay']
crop_types = ['wheat', 'maize', 'rice']

# Create a synthetic DataFrame with mock data for training
data = pd.DataFrame({
    'Soil Type': np.random.choice(soil_types, 1000),
    'Crop Type': np.random.choice(crop_types, 1000),
    'Nitrogen (N)': np.random.uniform(0, 100, 1000),
    'Phosphorus (P)': np.random.uniform(0, 100, 1000),
    'Potassium (K)': np.random.uniform(0, 100, 1000),
    'Rainfall (mm)': np.random.uniform(200, 1000, 1000),
    'Temperature (C)': np.random.uniform(15, 35, 1000),
    'pH Level': np.random.uniform(5.5, 8.5, 1000),
    'Area Size (ha)': np.random.uniform(1, 10, 1000),
})

# Create synthetic target values
data['Optimal N'] = np.random.uniform(50, 150, 1000)
data['Optimal P'] = np.random.uniform(30, 90, 1000)
data['Optimal K'] = np.random.uniform(30, 100, 1000)

# One-hot encode the categorical columns
data = pd.get_dummies(data, columns=['Soil Type', 'Crop Type'], drop_first=True)

# Separate features and target variables
X = data.drop(columns=['Optimal N', 'Optimal P', 'Optimal K'])
y = data[['Optimal N', 'Optimal P', 'Optimal K']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'fertilizer_model.pkl')

# Load the model back (this ensures it runs smoothly when deployed)
model = joblib.load('fertilizer_model.pkl')

@app.route('/')
def form():
    # Render the form page where users input data
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    soil_type = request.form['soil_type']
    crop_type = request.form['crop_type']
    nitrogen = float(request.form['nitrogen'])
    phosphorus = float(request.form['phosphorus'])
    potassium = float(request.form['potassium'])
    rainfall = float(request.form['rainfall'])
    temperature = float(request.form['temperature'])
    ph = float(request.form['ph'])
    area = float(request.form['area'])

    # One-hot encode categorical data according to the trained model's columns
    soil_encoded = [1 if soil_type == 'loamy' else 0, 1 if soil_type == 'sandy' else 0]
    crop_encoded = [1 if crop_type == 'maize' else 0, 1 if crop_type == 'rice' else 0]

    # Prepare the input array for prediction
    input_features = [nitrogen, phosphorus, potassium, rainfall, temperature, ph, area] + soil_encoded + crop_encoded
    input_data = np.array(input_features).reshape(1, -1)

    # Get the prediction from the model
    prediction = model.predict(input_data)
    predicted_n, predicted_p, predicted_k = prediction[0]

    # Render the result using the output.html page
    return render_template('output.html', predicted_n=predicted_n, predicted_p=predicted_p, predicted_k=predicted_k)

if __name__ == '__main__':
    app.run(debug=True)