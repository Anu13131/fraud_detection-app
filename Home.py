import streamlit as st

def run():
    st.markdown("<h1 style='text-align: center;'>🏦 WELCOME TO CREDIT CARD FRAUD DETECTION SOFTWARE</h1>", unsafe_allow_html=True)
    st.image("credit_card.jpg", use_container_width=True)

    st.markdown("""
        <div style='text-align: center; font-size: 18px;'>
        Securely manage your transactions and detect fraud in real-time. <br>
        Use the sidebar to navigate through the platform.
        </div>
    """, unsafe_allow_html=True)

    # Check if user is logged in
    if "user" in st.session_state:
        st.success(f"✅ Logged in as: **{st.session_state['user']['full_name']}**")
        if st.button("👤 View Profile"):
            st.switch_page("profile.py")  # Redirect to Profile Page
        if st.button("🚪 Logout"):
            del st.session_state["user"]
            st.rerun()
    else:
        st.button("🔐 Login")
        st.button("📝 Register")

if __name__ == "__main__":
    run()
