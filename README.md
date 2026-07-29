<div align="center">
  <h1>AmeriState</h1>
  <p><strong>AI-Powered US Real Estate Valuation & Market Analytics Platform</strong></p>
</div>

<br />

## 📖 Overview
**AmeriState** is a professional-grade PropTech application designed to accurately estimate the market value of residential real estate across the United States. Leveraging Machine Learning (Multiple Linear & Polynomial Regression), this platform processes critical property features such as square footage, neighborhood quality, and house age to deliver real-time, data-driven valuations.

This tool is tailored for Real Estate Analysts, Investors, and PropTech enthusiasts who need quick, reliable property assessments coupled with an intuitive Market Data Explorer.

## ✨ Features
- **📊 Interactive Data Explorer:** Conduct Exploratory Data Analysis (EDA) on US housing data using dynamic, premium Plotly charts. Visualize price distributions, correlations, and feature impacts instantly.
- **📈 Real-Time Model Diagnostics:** Monitor the AI model’s performance metrics (R², MAE, RMSE) transparently on the dashboard to ensure trust in the valuation algorithm.
- **🔮 Real-Time Price Predictor:** A sleek, user-friendly control panel allowing users to input property specifications and instantly receive an estimated market value, complete with variance analysis against market averages.
- **🚀 High-Performance Architecture:** Employs Streamlit's `@st.cache_resource` for zero-latency model inference and seamless UX.

## 🛠️ Technology Stack
- **Frontend / UI:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Linear Regression, StandardScaler)
- **Data Visualization:** Plotly (Express & Graph Objects)

## 📁 Project Structure
```text
AmeriState/
│
├── app.py                      # Main Streamlit Dashboard entry point
├── requirements.txt            # Python dependencies
│
├── src/                        # Source Code (Backend)
│   ├── __init__.py
│   ├── preprocessing.py        # Data pipeline (Formatting, Scaling, Feature Engineering)
│   └── model_inference.py      # Secure Model Loading and Prediction logic
│
├── models/                     # Serialized AI Models
│   ├── house_price_model.pkl   # Trained Regression Model
│   └── scaler.pkl              # Fitted StandardScaler
│
└── dataset/                    # Real Estate Market Data
    └── house_price_regression_dataset.csv
```

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your local machine.

### Installation & Execution
1. **Clone the repository**
   ```bash
   git clone git@github.com:yousefelgohary/AmeriState.git
   cd AmeriState
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the AmeriState Platform**
   ```bash
   streamlit run app.py
   ```
   The application will automatically launch in your default web browser at `http://localhost:8501`.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
