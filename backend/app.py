from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Load the model and scaler
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = data['features']

        # Convert input data to numpy array and scale
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        standardized_data = scaler.transform(input_data_reshaped)

        # Predict
        prediction = model.predict(standardized_data)
        result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)