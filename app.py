import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.teacher_screen import teacher_screen
from src.screen.student_screen import student_screen
from src.componet.header import header
from src.ui.style_base_layout import style_base_layout, style_hide, style_font

def main():
    if 'login-type' not in st.session_state:
        st.session_state['login-type'] = None
        # st.session_state.key = 'value'
    style_font()
    header()

    style_hide()
    style_base_layout()
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

    # st.markdown("""
    #             ### Heading `code`
    # """)
    
    # st.markdown("""
    #             <style>
    #                 button{
    #                 background : cyan !important;
    #             }
    #             </style>
    # <head>head </head>
    # <div> erf </div>
    
    # """, unsafe_allow_html=True)