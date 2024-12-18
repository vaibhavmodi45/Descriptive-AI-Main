# frontend.py
import streamlit as st
import requests
from PIL import Image, ImageFilter

# Page configuration
st.set_page_config(page_title="Descriptive AI", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>

    body {
        height: 100px;       
    }
    
    .navbar {
        margin-top: -50px;
        background-color: ;
        padding-left:2px;
        text-align: left;
        font-weight: bolder;
        font-size: 54px;
        color: black;
    }

    hr {
        margin-top: 8px;
        margin-bottom: 48px;
    }
    
    .generate-btn {
        background-color: #ff4b4b;
        border-radius: 5px;
        padding: 10px;
        color: white;
        font-weight: bold;
    }
    
    .steps-container {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 20px;
        margin-top: 150px;
    }
            
    .steps-container img {
        width: 80%;
        height: auto;
    }
            
    .steps-container h2 {
        font-size: 24px;
    }
    
    .footer {
        text-align: center;
        padding: 10px;
        background-color: #ff4b4c;
        color: white;
        margin-top: 100px;
        width: 100%;
        margin-bottom: 0;
    }
    
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">DESCRIPTIVE AI 📑 <hr></div>', unsafe_allow_html=True)

# Input field
user_input = st.text_input("Enter title or content")

# Generate button
if st.button("Generate"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/generate", json={"input_text": user_input})
        if response.status_code == 200:
            description = response.json().get('description', 'No description generated.')
            st.success(description)
        else:
            st.error("Error in generating description.")
    else:
        st.warning("Please enter some text.")

# Steps to use Descriptive AI
#st.markdown('<div class="steps-container">', unsafe_allow_html=True)
st.subheader("Steps to use Descriptive AI:")
st.markdown("1. Enter the appropriate title in the input field.")
st.image('1.png')
st.markdown("2. Click on the generate button.")
st.image('2.png')
st.markdown("3. Get your generated content displayed below.")
st.image('3.png')
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">All Rights Reserved <br> Developed by Team @Descriptive_AI</div>', unsafe_allow_html=True)