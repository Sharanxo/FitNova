import streamlit as st
from auth import register, login
from bmi import show_bmi
from pro import manage_profile
from workouts import log_workout
from tips import show_tip
from dashboard import show_dashboard
from goals import set_goal, view_goals
from report_generator import generate_user_report
from chatbot import fitness_chatbot, show_chat_analytics
from nutrition_chat import nutrition_chat  # ✅ Nutrition assistant

st.set_page_config("FitNova", layout="wide")

def main():
    if "user_id" not in st.session_state:
        page = st.sidebar.selectbox("Menu", ["Login", "Register"])
        if page == "Login":
            login()
        else:
            register()
    else:
        st.sidebar.image("logo.png", width=120)  
        st.sidebar.markdown(f"👋 Hello, **{st.session_state.user['name']}**")
        show_tip(st.session_state.user_id)
        
        st.markdown("""
        <div style='text-align:center; padding: 10px 0;'>
            <h2 style='color:#FF6B6B;'>🏋️ Welcome to <b>FitNova</b></h2>
            <p style='font-size:16px'>AI-powered fitness insights at your fingertips.</p>
        </div>
        """, unsafe_allow_html=True)

        choice = st.sidebar.radio(
            "📂 Navigation", 
            ["Dashboard", "BMI", "Profile", "Workout", "Goals", "Chatbot", "Nutrition", "Report", "Logout"]
        )

        if choice == "Logout":
            st.session_state.clear()
            st.experimental_rerun()

        elif choice == "Dashboard":
            show_dashboard(st.session_state.user_id)

        elif choice == "BMI":
            show_bmi(st.session_state.user)

        elif choice == "Profile":
            manage_profile(st.session_state.user_id)

        elif choice == "Workout":
            log_workout(st.session_state.user_id)

        elif choice == "Goals":
            set_goal(st.session_state.user_id)
            view_goals(st.session_state.user_id)

        elif choice == "Chatbot":
            fitness_chatbot(st.session_state.user_id)
            with st.expander("📊 My Chatbot Analytics"):
                show_chat_analytics(st.session_state.user_id)

        elif choice == "Nutrition":
            nutrition_chat(st.session_state.user_id)

        elif choice == "Report":
            if st.button("📄 Generate PDF Report"):
                path = generate_user_report(
                    st.session_state.user_id,
                    st.session_state.user['name']
                )
                with open(path, "rb") as f:
                    st.download_button("⬇️ Download", f, file_name=path, mime="application/pdf")

if __name__ == "__main__":
    main()
