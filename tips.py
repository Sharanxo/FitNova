import streamlit as st
from db import query_db
import random

def show_tip(user_id):
    tips = query_db("SELECT tip_text FROM tips", None)
    if tips:
        tip = random.choice(tips)['tip_text']
        st.info(f"💡 {tip}")
