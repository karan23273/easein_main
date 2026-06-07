import streamlit as st
import base64

def style_base_layout():
    st.markdown("""
        <style>
            .stApp{
            background: #58FAFC !important
        }
        </style>

    """, unsafe_allow_html=True)

def style_font():
    st.markdown(f"""
    <style>
        @font-face {{
        font-family: 'MyFont';
        src: url('https://your.cdn.example/GameOfThrones.ttf') format('truetype');
        font-display: swap;
        }}
        html, body, [class*="css-"], .stApp {{
        font-family: 'MyFont', Inter, sans-serif !important;
        }}
    </style>
    """, unsafe_allow_html=True)

def style_hide():
    st.markdown("""
        <style>
            #MainMenu, footer,header{
                visibility:hidden    
            }
            .block-container{
                padding-top: 1.5rem !important    
            }
        </style>

    """, unsafe_allow_html=True)