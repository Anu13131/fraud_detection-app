import streamlit as st
import mysql.connector

# Function to create a database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AnushkaDe@123",  # Replace with your MySQL password
        database="user_authentication"
    )

# Function to fetch user details
def get_user(email):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT full_name, email, password FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to update user details
def update_user(email, new_name, new_password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET full_name=%s, password=%s WHERE email=%s", (new_name, new_password, email))
    conn.commit()
    conn.close()
    return True

# Profile Page Function
def profile_page():
    """User Profile Page"""
    st.title("👤 My Profile")

    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.error("⚠️ Please log in to access your profile.")
        return

    email = st.session_state["user_email"]  # Fetch logged-in user's email
    user = get_user(email)

    if user:
        st.write(f"📧 **Email:** {user['email']}")
        new_name = st.text_input("👤 Full Name", value=user["full_name"])
        new_password = st.text_input("🔑 New Password", type="password", placeholder="Enter new password")

        if st.button("💾 Update Profile"):
            if update_user(email, new_name, new_password):
                st.success("✅ Profile updated successfully!")
            else:
                st.error("❌ Failed to update profile. Try again.")

    # Forgot Password Feature
    # st.markdown("---")
    # st.subheader("🔑 Forgot Password?")
    # reset_email = st.text_input("📧 Enter your registered email to reset password")

    # if st.button("🔄 Reset Password"):
    #     user = get_user(reset_email)
    #     if user:
    #         new_temp_password = "Temp@123"  # Generate a random temp password in real scenarios
    #         update_user(reset_email, user["full_name"], new_temp_password)
    #         st.success(f"✅ Temporary password set: **{new_temp_password}**. Please change it after login.")
    #     else:
    #         st.error("❌ Email not found. Please enter a registered email.")

if __name__ == "__main__":
    profile_page()
