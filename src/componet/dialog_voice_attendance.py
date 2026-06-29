import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from datetime import datetime 
from src.componet.dialog_attendance_results import attendance_result_dialog
import pandas as pd
from src.componet.dialog_attendance_results import show_attendance_result

@st.dialog("Voice attendance")
def voice_attendance_dialog(selected_subject_id, enrolled_students):
    st.write('Record audio file of students saying I am present, To AI recognition')

    audio_data = None 
    audio_data = st.audio_input("Record classroom audio")
    
    canditates_dict = {}
    for stu in enrolled_students:
        if stu['student']['voice_embedding']:
            canditates_dict[stu['id']] = stu['voice_embedding']
   
    if st.button('Analyze audio', width='stretch', type='primary'):
        with st.spinner("Processing audio file"):
            if not canditates_dict:
                st.error("No students enrolled in this course")
                return
            detetected_scores = process_bulk_audio(audio_data.read(), canditates_dict)

            results, attendance_to_log = [], []
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['student'] 
                scores = detetected_scores.get(student['student_id'], 0.0)
                is_present = bool(scores) > 0
                if is_present:
                    results.append({
                        'Name': student['student_name'],
                        'ID': student['student_id'],
                        'Source':scores if is_present else "-",
                        'Status': "Present" if is_present else "Absent"
                    })
                    attendance_to_log.append({
                        'student_id': student['student_id'],
                        'subject_id': selected_subject_id,
                        'timestamp':current_timestamp,
                        'is_present': bool(is_present)
                    })
            st.session_state.voice_attendance_result = pd.DataFrame(results), attendance_to_log
            # attendance_result_dialog(pd.DataFrame(results), attendance_to_log)
    if st.session_state.voice_attendance_result:
        st.divider()
        df_results, logs = st.session_state.voice_attendance_result
        show_attendance_result(df_results, logs)