import re
import streamlit as st

# Page styling
st.set_page_config(page_title="SecurePass - Password Strength Analyzer", page_icon="🛡️", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #e0f7ff !important;
        }
        .stTextInput>div>div>input {
            background-color: #f5faff !important;
            border: 2px solid #004aad !important;
            padding: 14px;
            border-radius: 12px;
            font-size: 18px;
        }
        .stButton button {
            width: 70%;
            background-color: #004aad !important;
            color: white !important;
            font-size: 22px;
            font-weight: bold;
            border-radius: 14px;
            padding: 16px;
            border: none;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #003080 !important;
        }
        .center-text {
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: #004aad;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.markdown("<h1 class='center-text'>🛡️ SecurePass - Password Strength Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-text'>🔎 Test your password's strength and receive expert recommendations for enhanced security.</p>", unsafe_allow_html=True)

# Password checking function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🚨 Your password must be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Include both uppercase and lowercase letters to strengthen security.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Add at least one number for extra protection.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔑 Use a special character (!@#$%^&*) to enhance security.")

    # Display password strength
    if score == 4:
        st.success("✅ **Excellent! Your password is very strong and well-protected.**")
    elif score == 3:
        st.info("🟡 **Good, but there's room for improvement!** Consider adding more security elements.")
    else:
        st.error("❌ **Weak Password!** Follow the recommendations below to improve it.")

    # Display feedback
    if feedback:
        with st.expander("💡 **Strengthen Your Password**"):
            for item in feedback:
                st.write(item)

# Password input
password = st.text_input("🔐 Enter Your Password", type="password", help="Ensure your password is strong and secure.")

# Button to check strength
if st.button("🔍 Analyze Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to analyze.")
