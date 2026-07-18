import streamlit as st
import pandas as pd
import pickle
import time

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="NJANASETU",
    page_icon="🎓",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
try:
    model = pickle.load(open("student_model.pkl", "rb"))
except:
    st.error("Model file missing or corrupted! Please generate student_model.pkl")
    st.stop()

# ---------------- CSS STYLING (Green–White Theme) ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f9fff9, #e8f5e9);
    }
    .main-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 100%;
    }
    .card {
        background: white;
        border-radius: 20px;
        padding: 40px 30px;
        margin: 20px auto;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 100, 0, 0.1);
        width: 90%;
        max-width: 600px;
    }
    .welcome-card {
        background: linear-gradient(135deg, #2e7d32 0%, #66bb6a 100%);
        color: white;
        border-radius: 20px;
        padding: 50px 30px;
        margin: 20px auto;
        text-align: center;
        box-shadow: 0 15px 30px rgba(46, 125, 50, 0.3);
        width: 90%;
        max-width: 600px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #43a047, #66bb6a);
        color: white;
        padding: 14px 35px;
        border-radius: 25px;
        border: none;
        font-size: 16px;
        font-weight: 600;
        margin: 12px 0;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(67, 160, 71, 0.4);
    }
    .progress-container {
        background: #e0f2f1;
        border-radius: 20px;
        overflow: hidden;
        height: 40px;
        margin: 25px 0;
    }
    .progress-bar {
        height: 100%;
        text-align: center;
        color: white;
        font-weight: bold;
        line-height: 40px;
        font-size: 16px;
        border-radius: 20px;
        background: linear-gradient(135deg, #66bb6a, #2e7d32);
    }
    .suggestion-card {
        background: #f9fff9;
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        border-left: 5px solid #43a047;
        width: 90%;
        max-width: 600px;
    }
    .stNumberInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #c8e6c9;
        padding: 12px 15px;
    }
    .stSelectbox>div>div>div {
        border-radius: 12px;
        border: 2px solid #c8e6c9;
    }
    .centered-column {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SUBJECTS ----------------
subjects = [
    "Mathematics for Information Science III",
    "Data Structures and Algorithms",
    "Foundation of Artificial Intelligence",
    "Introduction to Data Science",
    "Economics for Engineers",
    "Digital Electronics and Logic Design"
]

# ---------------- SUGGESTIONS FUNCTION ----------------
def get_suggestions(subject, score):
    suggestions = []
    if subject == "Mathematics for Information Science III":
        if score < 60: suggestions.append("Solve more practice problems 📚")
        if score < 50: suggestions.append("Revise formula sheets daily ✏️")
        if score < 40: suggestions.append("Consider one-on-one tutoring 🏫")
    elif subject == "Data Structures and Algorithms":
        if score < 60: suggestions.append("Practice coding on online platforms 💻")
        if score < 50: suggestions.append("Refer textbooks for complex topics 📖")
        if score < 40: suggestions.append("Redo previous assignments 📝")
    elif subject == "Digital Electronics and Logic Design":
        if score < 60: suggestions.append("Practice circuit problems regularly 🔌")
        if score < 50: suggestions.append("Revise logic gates and truth tables ⚡")
        if score < 40: suggestions.append("Work on lab exercises 🛠️")
    elif subject == "Foundation of Artificial Intelligence":
        if score < 60: suggestions.append("Understand AI concepts using case studies 🤖")
        if score < 50: suggestions.append("Rewatch lectures and practice examples 🧠")
        if score < 40: suggestions.append("Work on mini AI projects 🚀")
    elif subject == "Introduction to Data Science":
        if score < 60: suggestions.append("Practice data cleaning and analysis 📊")
        if score < 50: suggestions.append("Work with more datasets 🗂️")
        if score < 40: suggestions.append("Try Kaggle mini-projects 🏆")
    elif subject == "Economics for Engineers":
        if score < 60: suggestions.append("Revise economic principles 💹")
        if score < 50: suggestions.append("Work on sample problems 📝")
        if score < 40: suggestions.append("Attend extra lectures 👥")
    return suggestions

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ---------------- PAGE 1: WELCOME ----------------
if st.session_state.page == "welcome":
    st.markdown("""
    <div class="main-container">
        <div class="welcome-card">
            <h1>🎓 NJANASETU</h1>
            <p>Bridge to Academic Excellence</p>
            <p>AI-Powered Performance Prediction</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🌿 Start Your Journey", use_container_width=True):
        st.session_state.page = "department"
        st.rerun()

# ---------------- PAGE 2: DEPARTMENT ----------------
elif st.session_state.page == "department":
    st.markdown("""
    <div class="main-container">
        <div class="card">
            <h2>🎯 Department Verification</h2>
            <p>Are you a 3rd Semester AI & DS Student?</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_yes, col_no = st.columns(2, gap="medium")
    with col_yes:
        if st.button("✅ Yes", use_container_width=True):
            st.session_state.page = "subject"
            st.rerun()
    with col_no:
        if st.button("❌ No", use_container_width=True):
            st.error("This system is currently available for AI & DS students only")

# ---------------- PAGE 3: SUBJECT SELECTION ----------------
elif st.session_state.page == "subject":
    st.markdown("""
    <div class="main-container">
        <div class="card">
            <h2>📚 Choose Your Subject</h2>
            <p>Select the subject you want to analyze</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    subject = st.selectbox("Select your subject:", subjects)
    
    col_back, col_next = st.columns(2, gap="medium")
    with col_back:
        if st.button("⬅️ Back", use_container_width=True):
            st.session_state.page = "department"
            st.rerun()
    with col_next:
        if st.button("➡️ Continue", use_container_width=True):
            st.session_state.subject = subject
            st.session_state.page = "predict"
            st.rerun()

# ---------------- PAGE 4: PREDICTION ----------------
elif st.session_state.page == "predict":
    st.markdown(f"""
    <div class="main-container">
        <div class="card">
            <h2>📊 Performance Predictor</h2>
            <p>Analyzing: <strong>{st.session_state.subject}</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    hours = st.number_input("Weekly Study Hours ⏰", 0.0, 24.0, 6.0)
    attendance = st.number_input("Attendance Percentage 📅", 0, 100, 85)
    previous = st.number_input("Previous Exam Score 📝", 0, 100, 72)
    
    if st.button("🎯 Predict My Score", use_container_width=True):
        with st.spinner('🌱 Analyzing your academic progress...'):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i+1)
            
            data = pd.DataFrame([[hours, attendance, previous]],
                                columns=['Hours_Studied','Attendance','Previous_Scores'])
            predicted_score = model.predict(data)[0]
            model_error = 4.0
            
            st.markdown(f"""
            <div class="main-container">
                <div class="card">
                    <h3>Predicted Score: {predicted_score:.1f}/100</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width:{min(predicted_score, 100)}%">
                            {predicted_score:.1f}%
                        </div>
                    </div>
                    <p>Prediction Error Margin: ±{model_error}%</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if predicted_score >= 85:
                st.success("🎉 Excellent! Keep growing! 🌿")
            elif predicted_score >= 70:
                st.success("⭐ Great job! You're on track! 🌱")
            elif predicted_score >= 60:
                st.warning("💡 Doing well — a little more effort will help!")
            else:
                st.error("📚 Let’s focus on improving together 🌼")
            
            suggestions = get_suggestions(st.session_state.subject, predicted_score)
            if suggestions:
                st.markdown("""
                <div class="main-container">
                    <div class="suggestion-card">
                """, unsafe_allow_html=True)
                st.markdown("### 🌿 Personalized Suggestions:")
                for i, s in enumerate(suggestions, 1):
                    st.markdown(f"{i}. {s}")
                st.markdown('</div></div>', unsafe_allow_html=True)
            
            col_new, col_home = st.columns(2, gap="medium")
            with col_new:
                if st.button("🔄 New Prediction", use_container_width=True):
                    st.session_state.page = "subject"
                    st.rerun()
            with col_home:
                if st.button("🏠 Home", use_container_width=True):
                    st.session_state.page = "welcome"
                    st.rerun()
    
    if st.button("⬅️ Back to Subjects", use_container_width=True):
        st.session_state.page = "subject"
        st.rerun()