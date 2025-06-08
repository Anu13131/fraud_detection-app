import streamlit as st
import mysql.connector

# Function to create MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AnushkaDe@123",  # Replace with your password
        database="user_authentication"
    )

# Function to insert support message into DB
def insert_support_message(name, email, issue, message):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO support_messages (name, email, issue_type, message) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, issue, message))
    conn.commit()
    conn.close()

# UI
def run():
    st.markdown("""
        <style>
            .help-container {
                background-color: #f0f8ff;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                font-family: 'Segoe UI', sans-serif;
            }
            .help-heading {
                text-align: center;
                font-size: 2.5rem;
                color: #003366;
            }
            .help-content {
                font-size: 1.2rem;
                color: #333;
                text-align: center;
                margin-top: 1rem;
            }
        </style>

        <div class="help-container">
            <div class="help-heading">❓ Need Help?</div>
            <div class="help-content">
                Reach out to us anytime. Submit your issue using the form below.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📬 Contact Support Form")
    with st.form("support_form"):
        name = st.text_input("👤 Your Name")
        email = st.text_input("📧 Your Email")
        issue = st.selectbox("🔎 Select Issue", ["Login Issue", "Registration Problem", "Transaction Error", "General Inquiry"])
        message = st.text_area("📝 Your Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                insert_support_message(name, email, issue, message)
                st.success(f"✅ Thank you, {name}! Your message has been recorded.")
            else:
                st.error("⚠️ Please fill in all required fields.")

if __name__ == "__main__":
    run()
