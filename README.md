# Diamond Price Predictor

This project is a machine learning-powered web application that predicts the price of a diamond based on its physical characteristics.

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
