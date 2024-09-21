import numpy as np
import pandas as pd

def make_prediction(model, data):

    if model is None:
        raise ValueError("Model is not loaded. Cannot make predictions.")
    print(data.values)
    # Make the prediction
    try:
        prediction = model.predict(data.values)
        print("successfully predicted")
        return prediction
    except Exception as e:
        return str(e)
