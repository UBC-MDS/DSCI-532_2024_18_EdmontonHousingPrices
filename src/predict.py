import sys
sys.path.append('../')

import pandas as pd
import joblib

# Load the saved model
model = joblib.load('models/price_model.pkl')  # see the notebook notebooks/data_model.ipynb for model training details


def preprocess_data(data): # assumes the incoming data to be the same with the transformed data in observation.py
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