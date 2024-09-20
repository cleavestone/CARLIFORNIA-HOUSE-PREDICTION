from flask import Flask, request, jsonify, render_template
from src.data_preprocessing import preprocess_input
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
    try:
        # Get input data from the request
        input_data = request.json

        # Preprocess the input data
        processed_data = preprocess_input(input_data)

        # Make prediction
        prediction = make_prediction(model, processed_data)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)