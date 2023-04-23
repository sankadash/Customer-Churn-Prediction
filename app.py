import streamlit as st
import pandas as pd
import numpy as np
import joblib 

model = joblib.load('churn_model.pkl')
df = pd.read_csv("customer-churn-prediction-2020/train.csv")
encoders = joblib.load('encoders.pkl')

def app():
     st.title("Customer Churn Prediction")
     st.write("This is a simple app to predict customer churn")
     
     international_plan = st.selectbox("International Plan", df.international_plan.unique())
     voice_mail_plan = st.selectbox("Voice Mail Plan", df.voice_mail_plan.unique())
     number_vmail_messages = st.slider("Number of Voice Mail Messages", 0,40)
     total_intl_minutes = st.slider("Total International Minutes", min_value=0.0, max_value=17.25, value=0.0)
     
     total_intl_calls = st.slider("Total International Calls", min_value=0, max_value=11, value=0)
     total_intl_charge = st.slider("Total International Charge", min_value=0.0, max_value=4.65, value=0.0)
     
     number_customer_service_calls = st.slider("Number of Customer Service Calls", min_value=0, max_value=9, value=0)
     
     total_net_minutes = st.slider("Total Net Minutes", min_value=0.0, max_value=876.9, value=0.0)
     total_net_calls = st.slider("Total Net Calls", min_value=0, max_value=407, value=0)
     total_net_charge = st.slider("Total Net Charge", min_value=0.0, max_value=89.8475, value=0.0)
     ##write the predict function
     if st.button('Predict'):
               input_data = pd.DataFrame({'international_plan': [international_plan],'voice_mail_plan': [voice_mail_plan],'number_vmail_messages': [number_vmail_messages],'total_intl_minutes': [total_intl_minutes],'total_intl_calls': [total_intl_calls],'total_intl_charge': [total_intl_charge],'number_customer_service_calls': [number_customer_service_calls],'total_net_minutes':[total_net_minutes],'total_net_calls':[total_net_calls],'total_net_charge':[total_net_charge]}) 
               
               for col in encoders.keys():
                    input_data[col] = encoders[col].transform(input_data[col])[0]
               
               prediction = model.predict(input_data.values)
               if prediction[0] == 1:
                    st.write('High possibility that customers will continue ✅ using companies plan')
               else:
                    st.write('High possibility that customers will stop ❌ using companies plan')
                    
if __name__ == "__main__":
     app()
