import streamlit as st
from src.componet.header import header_home
from src.ui.base_layout import style_background_home
from src.ui.base_layout import style_background_home, style_hide, style_font

def home_screen():
    style_hide() # Hide 
    style_font() # common
    
    header_home()
    style_background_home()

    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.markdown(
            """
            <h3>I'm a Student</h3>
            <img src = 'https://i.ibb.co/844D9Lrt/mascot-student.png', style="width:130px; padding:0px 0px 0px 0px"/>
            
        """, unsafe_allow_html=True)
        if st.button('Login-as-Student', type="primary", key='1', width='stretch'):
            st.session_state['login-type'] = 'student'
            st.rerun()
    with col2:
        st.markdown(
            """
            <h3>I'm a Teacher</h3>
            <img src = 'https://i.ibb.co/CsmQQV6X/mascot-prof.png', style="width:160px; padding:0px 0px 1px 0px;"/>
            
        """, unsafe_allow_html=True)
        
        if st.button('Login-as-Teacher', type="primary", key='2', width='stretch'):
            st.session_state['login-type'] = 'teacher'
            st.rerun()

