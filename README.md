# Diamond Price Predictor

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

A machine learning-powered web application that predicts the price of a diamond based on its physical characteristics.

## Features
- Interactive UI using [Streamlit](https://jn4gpj55f5rckfavcmabbq.streamlit.app/).
- Trained using a `RandomForestRegressor` from `scikit-learn`.
- Predicts price based on:
  - Carat
  - Cut
  - Color
  - Clarity
  - Depth
  - Table
  - Dimensions (X, Y, Z)

## Performance Metrics

| Metric | Value |
| :--- | :--- |
| Mean Absolute Error (MAE) | 304.4488016578727 |
| Mean Squared Error (MSE) | 334680.72302214365 |
| Root Mean Squared Error (RMSE) | 578.5159660909486 |
| R-squared (R2) | 0.980121752481242 |
| Mean Absolute Percentage Error (MAPE) | 0.0852050534696888 |

## Prerequisites
- Python 3.x
- `pip`

## Installation

1. Clone the repository (or copy the files):
   ```bash
   git clone <repository-url>
   cd diamondPricePredictor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

## Dataset
This project uses the [Cubic Zirconia Dataset](https://www.kaggle.com/datasets/ronil8/diamond-price-prediction-dataset).
