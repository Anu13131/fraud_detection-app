import streamlit as st
import mysql.connector
import random
import string

# Function to create a database connection using Streamlit secrets
def create_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        port=st.secrets["mysql"]["port"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

# Function to check user credentials
def check_login(email, password):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT full_name, email FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to generate a random CAPTCHA
def generate_captcha(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

# Login Page Function
def login_page():
    """Secure Login Page with CAPTCHA & Database Authentication"""
    st.title("🔐 Secure Login Page")

    # Ensure CAPTCHA is initialized inside the function
    if "captcha" not in st.session_state:
        st.session_state["captcha"] = generate_captcha()

    email = st.text_input("📧 Email", placeholder="Enter your registered email")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    # Display CAPTCHA from session state
    st.write(f"🔢 CAPTCHA: **{st.session_state['captcha']}**")
    user_captcha = st.text_input("🔍 Enter CAPTCHA", placeholder="Type the CAPTCHA above")

    if st.button("Login"):
        user = check_login(email, password)

        if user:
            if user_captcha == st.session_state["captcha"]:
                st.success(f"✅ Welcome, {user['full_name']}!")
                st.session_state["authenticated"] = True  # Set authentication flag
                st.session_state["user_email"] = user["email"]
                st.session_state["user_name"] = user["full_name"]
            else:
                st.error("❌ Incorrect CAPTCHA. Please try again.")
        else:
            st.error("❌ Invalid email or password. Please try again.")

        # Generate a new CAPTCHA whether success or failure
        st.session_state["captcha"] = generate_captcha()

    # Refresh CAPTCHA Button
    if st.button("🔄 Refresh CAPTCHA"):
        st.session_state["captcha"] = generate_captcha()

if __name__ == "__main__":
    login_page()
