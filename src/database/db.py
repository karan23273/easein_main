from src.database.config import supabase
import bcrypt

def check_teacher_exist(teacher_user_name):
    # Check unique users returns false if user already exist
    response = supabase.table("teacher").select("teacher_user_name").eq('teacher_user_name', teacher_user_name).execute()
    return len(response.data) > 0

def hash_pass(user_password):
    return bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()

def match_pass(hashed, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed.code())

def create_teacher(teacher_user_name, teacher_name, teacher_user_pass):
    data ={
        'teacher_user_name': teacher_user_name,
        'teacher_pass': hash_pass(teacher_user_pass),
        'teacher_name' : teacher_name
    }
    response = supabase.table('teacher').insert(data).execute()
    return response.data

def teacher_login(teacher_user_name, teacher_user_pass):
    response = supabase.table('teacher').select('*').eql('teacher_user_name', teacher_user_name).execute()

    if response.data:
        teacher = response.data[0]
        if match_pass(teacher['teacher_pass'], teacher_user_pass):
            return teacher
    
    return None

    