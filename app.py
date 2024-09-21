from flask import Flask, request, jsonify, render_template
from src.data_preprocessing import preprocess
from src.model import load_model
from src.predict import make_prediction
import joblib

app = Flask(__name__)

# Load the model
model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
        # Get input data from the request
        input_data = request.json

        # Preprocess the input data
        processed_data = preprocess(input_data)
        # Make prediction
        prediction = make_prediction(model, processed_data)
        # Return the prediction as JSON
        prediction=prediction.tolist()
        
        # If prediction is a single value, return it directly
        if isinstance(prediction, list) and len(prediction) == 1:
            prediction = prediction[0]

        # Ensure the prediction is a number
        if not isinstance(prediction, (int, float)):
            return jsonify({'error': 'Invalid prediction format'}), 400

        return jsonify({'prediction': prediction})
        

    

if __name__ == '__main__':
    app.run(debug=True)