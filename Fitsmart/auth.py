import streamlit as st
import bcrypt
from db import query_db

def register():
    st.subheader("📝 Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    pwd = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        pwd_hash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        query_db("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
                 (name, email, pwd_hash.decode()), commit=True)
        st.success("Account created. Please log in.")

def login():
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        user = query_db("SELECT * FROM users WHERE email=%s", (email,), fetchone=True)
        if user and bcrypt.checkpw(pwd.encode(), user["password_hash"].encode()):
            st.session_state.user_id = user["id"]
            st.session_state.user = user
            st.success("Login successful!")
        else:
            st.error("Invalid credentials.")
