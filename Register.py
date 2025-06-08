import streamlit as st
import mysql.connector
from database import create_connection

def register_user(name, email, password):
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False  # If email already exists
    finally:
        conn.close()

def run():
    st.markdown("<h1 style='text-align: center;'>📝 Create an Account</h1>", unsafe_allow_html=True)
    
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email Address")
    password = st.text_input("🔑 Password", type="password")

    if st.button("📝 Register"):
        success = register_user(name, email, password)
        if success:
            st.success("✅ Registration Successful! You can now login.")
        else:
            st.error("❌ Email already registered. Try another one.")

if __name__ == "__main__":
    run()
