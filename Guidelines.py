import streamlit as st

def run():
    st.markdown("<h1 style='text-align: center; color:#0a58ca;'>📜 Security Guidelines</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .guideline-box {
        background-color: #f0f8ff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 6px solid #0a58ca;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    guidelines = [
        "🔐 Use strong and unique passwords. Avoid using your name, birthdate, or simple combinations like '1234'.",
        "🛡️ Never share your OTP, CVV, or PIN with anyone—even if they claim to be from the bank.",
        "📧 Be cautious of phishing emails and fake websites. Always verify links before clicking.",
        "📱 Enable two-factor authentication (2FA) wherever possible for extra protection.",
        "🔍 Monitor your account activity regularly to spot unauthorized transactions early.",
        "💳 Avoid using public Wi-Fi while accessing banking services or making financial transactions.",
        "🔒 Log out of banking websites and apps after every session, especially on shared devices.",
        "🚨 Report any suspicious transactions or activities to the bank immediately.",
        "✅ Keep your devices' antivirus and OS updated to prevent malware threats.",
        "🌐 Always ensure you're on the official bank website before entering credentials.",
    ]

    for tip in guidelines:
        st.markdown(f"<div class='guideline-box'>{tip}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    run()
