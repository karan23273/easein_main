import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_font,style_hide
from src.componet.header import header_dashboard
from src.database.db import check_teacher_exist, create_teacher, teacher_login
import time

def teacher_screen():
    style_background_dashboard()
    style_font() 
    style_hide() 
    
    if 'teacher_data' in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()



######################################################## LOGIN #########################################################################
def login_teacher(teacher_user_name, teacher_user_pass):
    if not teacher_user_name or not teacher_user_pass:
        return False
        
    teacher = teacher_login(teacher_user_name, teacher_user_pass)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.isLogin = True
        return True
    return False

def teacher_screen_login():
    c1,c4 = st.columns([3,1], vertical_alignment='center', gap='xxlarge', width='stretch')
    with c4:
        if st.button('Back', type='tertiary', key='back-login', width='stretch'):
            st.session_state['login-type'] = None
            st.rerun()
    with c1:
        header_dashboard()


    st.markdown(f"""
        <h3 style= "font-size:25px; text-align:center">Login using password</h3>

    """, unsafe_allow_html=True)

    # input
    teacher_user_name = st.text_input('Enter your user name', placeholder='JohnDoe@iiitd')
    teacher_user_pass = st.text_input('Enter your password', type='password', placeholder='Password')
    st.divider()

    button1, button2 = st.columns([3,1], vertical_alignment='center', gap='xxlarge', width='stretch')
    
    login_success = -1
    with button2:
        if(st.button('Login', type='primary', key='login', width='stretch')):
            if login_teacher(teacher_user_name, teacher_user_pass):
                login_success = 1
            else:
                login_success = 0

    if login_success == 1:
        st.toast("Welcome, Sir", icon='🔥')
        time.sleep(0.5)
        st.rerun()
    elif login_success == 0:
        st.error("Username or Password is incorrect!")



    with button1:
        if(st.button('Register Instead', type='primary', key='register-instead', width='content')):
            st.session_state['teacher_login_type'] = 'register'
            st.rerun()

####################################################### REGISTER ###########################################################################

def register_teacher(teacher_user_name, teacher_name, teacher_user_pass, teacher_pass_confirm):
    if not teacher_name or not teacher_user_name or not teacher_user_pass or not teacher_pass_confirm:
        return False, "All fields are Mandatory"
    
    if check_teacher_exist(teacher_user_name):
        return False, "User already exist change username or try Login"

    if teacher_pass_confirm != teacher_user_pass:
        return False, "Password does not match"
    
    try:
        create_teacher(teacher_user_name, teacher_name, teacher_user_pass)
        return True, "Successfully Registered"
    except Exception as e:
        return False, "Unexpected Error"

def teacher_screen_register():
    c1,c4 = st.columns([3,1], vertical_alignment='center', gap='xxlarge', width='stretch')
    with c4:
        if st.button('Back', type='tertiary', key='back-register', width='stretch'):
            st.session_state['login-type'] = None
            st.rerun()
    with c1:
        header_dashboard()
    
    
    st.markdown(f""" 
        <h3 style= "font-size:25px; text-align:center">Register your teacher profile</h3>   """, unsafe_allow_html=True)
    
    teacher_user_name = st.text_input('Enter username', placeholder='JohnDoe@iiitd')
    teacher_name = st.text_input('Enter name', placeholder='John Doe')
    teacher_user_pass = st.text_input('Enter your password', type='password', placeholder='Password')
    teacher_pass_confirm = st.text_input('Confirm password', type='password', placeholder='Password')
    st.divider()

    button1, button2 = st.columns([3,1], vertical_alignment='center', gap='xxlarge', width='stretch')
    

    success = -1
    message = ""
    with button2:
        if(st.button('Register now', type='primary', key='register', width='stretch')):
            success, message = register_teacher(teacher_user_name, teacher_name, teacher_user_pass, teacher_pass_confirm)
    
    if success == 1:
        st.success(message)
        st.session_state.teacher_login_type = 'login'
        time.sleep(1.5)
        st.rerun()
    elif success == 0:
        st.error(message)


    with button1:
        if(st.button('Login Instead', type='primary', key='login-instead', width='content')):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()


################################################## TEACHER DASHBOARD ######################################################

def teacher_dashboard():
    teacher = st.session_state.teacher_data
    st.header(f"""
        Welcome,{teacher['teacher_name']}
    """)
    