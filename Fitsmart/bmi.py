import streamlit as st

def show_bmi(user):
    st.subheader("🧮 BMI Calculator")
    weight = st.number_input("Weight (kg)", value=user.get("weight") or 70.0)
    height_cm = st.number_input("Height (cm)", value=user.get("height") or 170.0)
    if st.button("Calculate BMI"):
        h = height_cm / 100
        bmi = weight / (h * h)
        category = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
        st.success(f"Your BMI is **{bmi:.2f}** — *{category}*")
