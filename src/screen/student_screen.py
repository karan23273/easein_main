import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_font,style_hide
from src.componet.header import header_dashboard
from src.database.db import check_teacher_exist, create_teacher, teacher_login
import time
from PIL import Image
import numpy as np


def student_screen():
    style_background_dashboard()
    style_font() 
    style_hide() 
    
    c1,c4 = st.columns([3,1], vertical_alignment='center', gap='xxlarge', width='stretch')
    with c4:
        if st.button('Back', type='tertiary', key='back-login', width='stretch'):
            st.session_state['login-type'] = None
            st.rerun()
    with c1:
        header_dashboard()
    
    
    st.markdown(f"""
        <h3 style= "font-size:25px; text-align:center">Login using face ID</h3>
    """, unsafe_allow_html=True)
    photo_source = st.camera_input("Keep your face in the center")

    if photo_source:
        imag = np.array(Image.open(photo_source))

        # more like loading circle
        with st.spinner('AI is scanning...'):
            
