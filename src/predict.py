import numpy as np

def make_prediction(model, data):
    """
    Make a prediction using the loaded model.
    
    Parameters:
    - model: The trained model object
    - data: Input data for prediction (as a NumPy array or similar)

    Returns:
    - Prediction result
    """
    if model is None:
        raise ValueError("Model is not loaded. Cannot make predictions.")
    
    # Ensure the input data is in the correct format (e.g., 2D array)
    if isinstance(data, list):
        data = np.array(data).reshape(1, -1)  # Reshape for a single data point
    
    prediction = model.predict(data)
    return prediction