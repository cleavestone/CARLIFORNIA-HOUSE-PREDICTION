import joblib
import os
import numpy as np

MODEL_PATH=r'C:\Users\Hp\Desktop\HOUSE_PREDICTION_APP\models\xgboost.joblib'


def load_model():
    """Load the trained model from the pkl file."""
    try:
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully!")
        return model
    except FileNotFoundError:
        print(f"Model file not found at {MODEL_PATH}")
        return None