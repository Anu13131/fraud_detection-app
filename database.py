import mysql.connector
import streamlit as st

# Function to create a database connection
def create_connection():
     return mysql.connector.connect(
        host=st.secrets["shinkansen.proxy.rlwy.net"],
        user=st.secrets["root"],
        password=st.secrets["YdezWoMvvsmuZqJAgUuxwZULUzuhbGJS"],
        database=st.secrets["fraud-detection-db"],
        port=st.secrets["26694"]
    )

# Function to create the users table if it doesn't exist
def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Call this function when the app starts
create_users_table()
