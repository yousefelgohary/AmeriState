import streamlit as st
import joblib

@st.cache_resource
def load_model_and_scaler():
    """
    Loads the trained model and scaler from the models directory.
    Uses @st.cache_resource to load these into memory only once,
    preventing reload on every user interaction.
    """
    try:
        model = joblib.load('models/house_price_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        return model, scaler
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

def predict_price(model, preprocessed_data):
    """
    Takes the model and preprocessed data and returns the predicted price.
    """
    prediction = model.predict(preprocessed_data)
    return prediction[0]
