import streamlit as st
import pandas as pd
import pickle

# Load trained model
model_path = "Pickle/Model.pkl"
if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))
else:
    st.error("❌ Model file not found. Please check your path.")
    st.stop()


st.title("📊 Sales Forecasting App")
st.write("Predict sales based on product and outlet information")

# User inputs
item_weight = st.number_input("Item Weight", min_value=0.0, max_value=50.0, value=10.0)
item_visibility = st.number_input("Item Visibility", min_value=0.0, max_value=1.0, value=0.05)
item_mrp = st.number_input("Item MRP", min_value=0.0, max_value=500.0, value=150.0)
outlet_years = st.number_input("Outlet Years of Operation", min_value=0, max_value=50, value=10)

# When the user clicks "Predict"
if st.button("Predict Sales"):
    input_data = pd.DataFrame({
        'Item_Weight': [item_weight],
        'Item_Visibility': [item_visibility],
        'Item_MRP': [item_mrp],
        'Outlet_Years': [outlet_years]
    })
    
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Sales: {prediction[0]:.2f}")
