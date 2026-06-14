import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.teacher_screen import teacher_screen
from src.screen.student_screen import student_screen
from src.ui.base_layout import style_hide, style_font


def main():
    if 'login-type' not in st.session_state:
        st.session_state['login-type'] = None
        # st.session_state.key = 'value'

    # common layout applied to every screen so edges align
    style_hide()
    style_font()

    match st.session_state['login-type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()
 
main()

    # name = st.text_input("Enter your name: ")

    # col1, col2 = st.columns(2, gap="xxsmall")
    # with col1:
    #     if st.button("fuck me", type="primary", key='1', width='stretch'):
    #         print("segx")
    # with col2:
    #     if st.button("fuck you", type="primary", key='2', width='content'):
    #         print("ohh yeah")
