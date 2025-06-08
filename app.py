import streamlit as st
import pickle
import numpy as np

def run():
    st.markdown("<h1 style='text-align: center;'>🔍 Credit Card Fraud Detection</h1>", unsafe_allow_html=True)
    st.image("transaction-fraud.jpg", use_container_width=True)

    st.markdown("### Enter Transaction Details:")
    input_df = st.text_input("🔢 Enter all transaction details (comma-separated): ")
    
    submit = st.button("🚀 Verify Transaction")

    if submit:
        try:
            model = pickle.load(open('model.pkl', 'rb'))
            features = np.asarray(input_df.split(','), dtype=np.float64)

            if len(features) != model.n_features_in_:
                st.error(f"⚠️ Error: Model expects {model.n_features_in_} features, but got {len(features)}")
            else:
                prob = model.predict_proba(features.reshape(1, -1))[:, 1]
                threshold = 0.1
                prediction = (prob > threshold).astype(int)

                st.success(f"🔹 Fraud Probability: **{prob[0]:.4f}**")
                if prediction[0] == 0:
                    st.success("✅ Legitimate Transaction")
                else:
                    st.error("🚨 Fraudulent Transaction Detected!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    run()
