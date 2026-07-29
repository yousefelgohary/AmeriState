import numpy as np
import pandas as pd

def format_input_data(square_footage, num_bedrooms, num_bathrooms, year_built, lot_size, garage_size, neighborhood_quality):
    """
    Formats the input variables into a pandas DataFrame matching the model's training data.
    """
    input_data = {
        'Square_Footage': [square_footage],
        'Num_Bedrooms': [num_bedrooms],
        'Num_Bathrooms': [num_bathrooms],
        'House_Age': [2024 - year_built],
        'Lot_Size': [lot_size],
        'Garage_Size': [garage_size],
        'Neighborhood_Quality': [neighborhood_quality]
    }
    return pd.DataFrame(input_data)

def preprocess_data(input_df, scaler):
    """
    Scales the input data using the fitted scaler.
    """
    scaled_data = scaler.transform(input_df)
    return scaled_data
