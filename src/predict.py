import sys
sys.path.append('../')

import pandas as pd
import joblib

# Load the saved model
model = joblib.load('models/price_model.pkl')  # see the notebook notebooks/data_model.ipynb for model training details


def preprocess_data(data): # assumes the incoming data to be the same with the transformed data in observation.py
    # Predefined summary statistics
    mean_values = {
        'longitude': -123.112161,
        'latitude': 49.262765,
        'accommodates': 3.545970,
        'beds': 1.933792,
        'bathroom_adjusted': 1.351025
    }
    mode_values = {
        'room_type': 'Entire home/apt'  # Most common value
    }

    # Fill missing values with predefined means for numerical columns
    for column, mean_value in mean_values.items():
        data[column].fillna(mean_value, inplace=True)
    
    # Fill missing values with predefined mode for categorical columns
    for column, mode_value in mode_values.items():
        data[column].fillna(mode_value, inplace=True)

    # Ensure that the categorical variables are encoded appropriately
    data['room_type'] = data['room_type'].astype('category')
    return data

def predict_price(data):
    # Preprocess the input data
    preprocessed_data = preprocess_data(data)
    # Make predictions using the model
    predictions = model.predict(preprocessed_data)
    
    return predictions

if __name__ == "__main__":
    # see this example usage when the script is directly run
    new_data = pd.DataFrame({
        'longitude': [-123.105090],
        'latitude': [49.247730],
        'accommodates': [4],
        'room_type': ['Entire home/apt'],
        'beds': [3.0],
        'bathroom_adjusted': [2.0]
    })

    # Make predictions
    prediction = predict_price(new_data)
    print("Predicted Price:", prediction)