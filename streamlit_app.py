import streamlit as st
import joblib
import numpy as np
model = joblib.load('predictor.pkl')
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    cutDict = {
        'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4
    }
    colorDict = {
        'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6
    }
    clarityDict = {
        'I3': 0, 'I2': 1, 'I1': 2, 'SI2': 3, 'SI1': 4, 'VS2': 5, 'VS1': 6, 'VVS2': 7, 'VVS1': 8, 'IF': 9, 'FL': 10
    }
    arr = np.array([
        carat, cutDict[cut], colorDict[color], clarityDict[clarity], depth, table, x, y, z
    ])
    arr = arr.reshape(1, -1)
    pred = model.predict(arr)
    return pred[0]
st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎")
st.title("💎 Diamond Price Predictor")
st.write("Welcome to our diamond price predictor! Please enter the physical characteristics of the diamond to estimate its price.")
col1, col2 = st.columns(2)
with col1:
    carat = st.number_input('Carat', min_value=0.0, value=0.34, step=0.01)
    cut = st.selectbox('Cut', ['Ideal', 'Fair', 'Good', 'Very Good', 'Premium'])
    color = st.selectbox('Color', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox('Clarity', ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL'])
with col2:
    depth = st.number_input('Depth', min_value=0.0, value=60.0, step=0.1)
    table = st.number_input("Table", min_value=0.0, value=56.0, step=0.1)
    x = st.number_input("X", min_value=0.0, value=5.3, step=0.1)
    y = st.number_input("Y", min_value=0.0, value=3.4, step=0.1)
    z = st.number_input("Z", min_value=0.0, value=3.9, step=0.1)
st.write("Please note that the predicted price is an estimate and may vary.")
if st.button("Predict Price", type="primary"):
    price = predict_price(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f"The estimated price of the diamond is: ${price:,.2f}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='color: gray;'>Made by bruzz-bruzz</p>
        <a href='https://github.com/bruzz-bruzz' target='_blank'>GitHub Profile</a> | 
        <a href='https://github.com/bruzz-bruzz/diamondPricePredictor' target='_blank'>GitHub Repository</a>
    </div>
    """,
    unsafe_allow_html=True
)

