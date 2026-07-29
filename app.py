import streamlit as st
import pandas as st_pd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Import backend modules
from src.preprocessing import format_input_data, preprocess_data
from src.model_inference import load_model_and_scaler, predict_price

# Configure the page
st.set_page_config(
    page_title="AmeriState | US Real Estate Valuation",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a more premium look
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .st-emotion-cache-1y4p8pa {
        padding: 2rem 1rem;
    }
    .metric-container {
        background-color: #1E2638;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)


# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/house_price_regression_dataset.csv')
    return df

df = load_data()

# Load Model
model, scaler = load_model_and_scaler()

# Application Header
st.title("AmeriState")
st.markdown("**AI-Powered US Real Estate Valuation & Market Analytics Platform**")
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs([
    "📊 Data Explorer & EDA", 
    "📈 Model Evaluation Metrics", 
    "🔮 Real-Time Price Predictor"
])

with tab1:
    st.header("Data Explorer & Market Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Price Distribution")
        fig_dist = px.histogram(df, x="House_Price", nbins=50, 
                              title="Distribution of House Prices",
                              color_discrete_sequence=['#0052cc'])
        fig_dist.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_dist, use_container_width=True)
        
    with col2:
        st.subheader("Price vs. Square Footage")
        fig_scatter = px.scatter(df, x="Square_Footage", y="House_Price", 
                               color="Neighborhood_Quality",
                               title="House Price based on Size & Neighborhood",
                               color_continuous_scale="Blues")
        fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    st.subheader("Feature Correlation Matrix")
    corr = df.corr()
    fig_corr = px.imshow(corr, text_auto=".2f", aspect="auto", 
                         color_continuous_scale="Blues",
                         title="Correlation between Features and Price")
    fig_corr.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_corr, use_container_width=True)

with tab2:
    st.header("Model Evaluation & Diagnostics")
    
    if model is not None and scaler is not None:
        # Generate predictions on the entire dataset for evaluation
        X = df.drop('House_Price', axis=1).copy()
        X['House_Age'] = 2024 - X['Year_Built']
        X = X.drop('Year_Built', axis=1)
        # Ensure column order matches the model's expected order
        X = X[['Square_Footage', 'Num_Bedrooms', 'Num_Bathrooms', 'House_Age', 'Lot_Size', 'Garage_Size', 'Neighborhood_Quality']]
        y = df['House_Price']
        
        X_scaled = scaler.transform(X)
        y_pred = model.predict(X_scaled)
        
        mae = mean_absolute_error(y, y_pred)
        rmse = np.sqrt(mean_squared_error(y, y_pred))
        r2 = r2_score(y, y_pred)
        
        st.markdown("### Performance Metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="R² Score", value=f"{r2:.4f}", delta="Accuracy")
        with col2:
            st.metric(label="Mean Absolute Error (MAE)", value=f"${mae:,.2f}", delta="-Error", delta_color="inverse")
        with col3:
            st.metric(label="Root Mean Squared Error (RMSE)", value=f"${rmse:,.2f}", delta="-Error", delta_color="inverse")
            
        st.markdown("---")
        
        st.subheader("Predicted vs Actual Prices")
        fig_eval = px.scatter(x=y, y=y_pred, labels={'x': 'Actual Price', 'y': 'Predicted Price'},
                             title="Model Accuracy: Actual vs Predicted",
                             opacity=0.6, color_discrete_sequence=['#0052cc'])
        # Add perfect prediction line
        fig_eval.add_trace(go.Scatter(x=[y.min(), y.max()], y=[y.min(), y.max()],
                                    mode='lines', name='Perfect Prediction',
                                    line=dict(color='red', dash='dash')))
        fig_eval.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_eval, use_container_width=True)
    else:
        st.error("Model or Scaler failed to load. Please check the models directory.")

with tab3:
    st.header("Real-Time Price Predictor")
    st.markdown("Enter property details below to instantly estimate the market value.")
    
    with st.form("prediction_form"):
        st.subheader("Property Specifications")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sq_ft = st.number_input("Square Footage", min_value=500, max_value=10000, value=2500, step=100)
            beds = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3, step=1)
            baths = st.number_input("Number of Bathrooms", min_value=1, max_value=8, value=2, step=1)
            
        with col2:
            year_built = st.number_input("Year Built", min_value=1800, max_value=2024, value=2000, step=1)
            lot_size = st.number_input("Lot Size (Acres)", min_value=0.1, max_value=20.0, value=2.0, step=0.1)
            
        with col3:
            garage = st.number_input("Garage Size (Cars)", min_value=0, max_value=5, value=2, step=1)
            neighborhood = st.slider("Neighborhood Quality", min_value=1, max_value=10, value=5, help="1 = Poor, 10 = Excellent")
            
        submit_button = st.form_submit_button("🔮 Predict Property Value", use_container_width=True)
        
    if submit_button:
        if model is None or scaler is None:
            st.error("Model engine is currently unavailable.")
        else:
            with st.spinner("Analyzing market data..."):
                # Prepare and predict
                input_df = format_input_data(sq_ft, beds, baths, year_built, lot_size, garage, neighborhood)
                scaled_input = preprocess_data(input_df, scaler)
                predicted_price = predict_price(model, scaled_input)
                
                # Compare to dataset average
                avg_price = df['House_Price'].mean()
                diff = predicted_price - avg_price
                
                st.success("Analysis Complete!")
                st.markdown("### Estimated Market Value")
                st.metric(
                    label="Predicted House Price",
                    value=f"${predicted_price:,.2f}",
                    delta=f"{diff:,.2f} vs Market Avg"
                )
