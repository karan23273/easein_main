import streamlit as st

def home_screen():
    st.header('I am a Home')

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button('Login-as-Student', type="primary", key='1', width='stretch'):
            st.session_state['login-type'] = 'student'
            st.rerun()
    with col2:
        if st.button('Login-as-Teacher', type="primary", key='2', width='stretch'):
            st.session_state['login-type'] = 'teacher'
            st.rerun()

