import streamlit as st
from db import query_db
import bcrypt

def manage_profile(user_id):
    st.subheader("🧑‍💻 Manage Profile")
    user = query_db("SELECT * FROM users WHERE id=%s", (user_id,), fetchone=True)
    name = st.text_input("Name", user['name'])
    age = st.number_input("Age", value=user.get("age") or 18)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0)
    weight = st.number_input("Weight (kg)", value=user.get("weight") or 70.0)
    height = st.number_input("Height (cm)", value=user.get("height") or 170.0)
    new_pwd = st.text_input("New Password", type="password")

    if st.button("Update"):
        query_db("UPDATE users SET name=%s, age=%s, gender=%s, weight=%s, height=%s WHERE id=%s",
                 (name, age, gender, weight, height, user_id), commit=True)
        if new_pwd:
            hashed = bcrypt.hashpw(new_pwd.encode(), bcrypt.gensalt()).decode()
            query_db("UPDATE users SET password_hash=%s WHERE id=%s", (hashed, user_id), commit=True)
        st.success("Profile updated!")
