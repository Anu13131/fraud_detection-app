import streamlit as st
from streamlit_option_menu import option_menu

import Home, Login, Register, app, Help, Guidelines, user_profile  # Import profile module

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Sidebar navigation
with st.sidebar:
    st.image("Fraud_prevention.png", use_container_width=True)
    
    selected = option_menu(
        menu_title="🏦 Banking Services",
        options=["Home", "Login", "Register", "Verify Transaction", "Profile", "Help", "Guidelines"],
        icons=["house", "key", "person-plus", "credit-card", "user", "question-circle", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )

# Load the selected page
if selected == "Home":
    Home.run()  # ✅ Correct function name
elif selected == "Login":
    Login.login_page()
elif selected == "Register":
    Register.run()
elif selected == "Verify Transaction":
    app.run()
elif selected == "Profile":
    user_profile.profile_page()  # Load Profile Page
elif selected == "Help":
    Help.run()
elif selected == "Guidelines":
    Guidelines.run()
