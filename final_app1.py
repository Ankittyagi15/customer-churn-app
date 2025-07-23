import streamlit as st
import numpy as np
import pickle

with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="📉 Customer Churn Predictor", layout="centered")
st.title("📞 Customer Churn Prediction App")
st.markdown("Enter customer details to predict if the customer is likely to churn.")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (in months)", 0, 72, 12)
phoneservice = st.selectbox("Phone Service", ["Yes", "No"])
multiplelines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
onlinesecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
onlinebackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
deviceprotection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
techsupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streamingtv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streamingmovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperlessbilling = st.selectbox("Paperless Billing", ["Yes", "No"])
paymentmethod = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthlycharges = st.number_input("Monthly Charges", min_value=0.0)
totalcharges = st.number_input("Total Charges", min_value=0.0)

binary_map = {'Yes': 1, 'No': 0, 'Female': 0, 'Male': 1}
input_data = [
    binary_map[gender],
    binary_map[senior],
    binary_map[partner],
    binary_map[dependents],
    tenure,
    binary_map[phoneservice],
    monthlycharges,
    totalcharges,
    binary_map[paperlessbilling],
    1 if multiplelines == 'Yes' else 0,
    1 if multiplelines == 'No phone service' else 0,
    1 if internet == 'Fiber optic' else 0,
    1 if internet == 'No' else 0,
    1 if onlinesecurity == 'No' else 0,
    1 if onlinesecurity == 'No internet service' else 0,
    1 if onlinebackup == 'No' else 0,
    1 if onlinebackup == 'No internet service' else 0,
    1 if deviceprotection == 'No' else 0,
    1 if deviceprotection == 'No internet service' else 0,
    1 if techsupport == 'No' else 0,
    1 if techsupport == 'No internet service' else 0,
    1 if streamingtv == 'No' else 0,
    1 if streamingtv == 'No internet service' else 0,
    1 if streamingmovies == 'No' else 0,
    1 if streamingmovies == 'No internet service' else 0,
    1 if contract == 'One year' else 0,
    1 if contract == 'Two year' else 0,
    1 if paymentmethod == 'Electronic check' else 0,
    1 if paymentmethod == 'Mailed check' else 0,
    1 if paymentmethod == 'Credit card (automatic)' else 0,
]

final_input = np.array([input_data])

if st.button("Predict"):
    prediction = model.predict(final_input)[0]
    if prediction == 1:
        st.warning("🟡 This customer is likely to churn.")
    else:
        st.success("🟢 This customer is likely to stay.")
