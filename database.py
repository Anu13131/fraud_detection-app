import mysql.connector
import streamlit as st

# Function to create a database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="AnushkaDe@123",  # 🔹 Change this to your MySQL password
        database="user_authentication"
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
