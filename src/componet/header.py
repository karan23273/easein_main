import streamlit as st
import pathlib
import base64

def header_home():
    logo_bytes = pathlib.Path('src/assets/attendance.png').read_bytes()
    logo_b64 = base64.b64encode(logo_bytes).decode()

    st.markdown(
        f"""
        <div style = 'display:flex; flex-direction: column; align-items:center; justify-content:center'>
            <img src="data:image/png;base64,{logo_b64}" style = 'height: 150px;'margin:0px;'/>
            <h1 style = 'text-align:center; color:#DDDDDD '>Ease IN</h1>
        </div>
        
    """, unsafe_allow_html=True)
def header_dashboard():
    logo_bytes = pathlib.Path('src/assets/attendance.png').read_bytes()
    logo_b64 = base64.b64encode(logo_bytes).decode()

    st.markdown(
        f"""
        <div style = 'display:flex; align-items:center; justify-content:flex-start; gap:20px'>
            <img src="data:image/png;base64,{logo_b64}" style = 'height: 60px;'/>
            <h2 class="dash-title" style = "text-align:center; font-size:20px; color: black; margin:0; white-space:nowrap;">
            Ease IN
            </h2>
        </div>
        
    """, unsafe_allow_html=True)

