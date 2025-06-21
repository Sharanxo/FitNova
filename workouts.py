import streamlit as st
from db import query_db
from datetime import date

calories_per_min = {
    "Running": 11.4,
    "Walking": 4.0,
    "Cycling": 8.5,
    "Yoga": 3.0,
    "Strength Training": 6.0,
    "HIIT": 12.0,
    "Swimming": 9.5,
    "Dancing": 5.5,
    "Jump Rope": 10.0,
    "Other": 5.0 
}

def log_workout(user_id):
    st.subheader("🏋️ Log Workout")

    exercise_type = st.selectbox("Select Exercise Type", list(calories_per_min.keys()))

    if exercise_type == "Other":
        exercise = st.text_input("Enter Custom Exercise")
    else:
        exercise = exercise_type

    duration = st.number_input("Duration (mins)", min_value=1)

    if exercise:
        estimated_calories = round(calories_per_min.get(exercise_type, 5.0) * duration)
        st.info(f"Estimated Calories Burned: {estimated_calories} kcal")

        if st.button("Save"):
            # Save workout log
            query_db(
                "INSERT INTO workouts (user_id, date, exercise, duration, calories_burned) VALUES (%s, %s, %s, %s, %s)",
                (user_id, date.today(), exercise, duration, estimated_calories),
                commit=True
            )

            query_db(
                """
                UPDATE goals
                SET current_value = current_value + %s
                WHERE user_id = %s AND goal_type = %s
                """,
                (duration, user_id, exercise),
                commit=True
            )

            query_db(
                """
                UPDATE goals
                SET status = 'Completed'
                WHERE user_id = %s AND goal_type = %s AND current_value >= target_value
                """,
                (user_id, exercise),
                commit=True
            )

            query_db(
                """
                UPDATE goals
                SET current_value = current_value + %s
                WHERE user_id = %s AND goal_type = 'Calories Burned'
                """,
                (estimated_calories, user_id),
                commit=True
            )

            query_db(
                """
                UPDATE goals
                SET status = 'Completed'
                WHERE user_id = %s AND goal_type = 'Calories Burned' AND current_value >= target_value
                """,
                (user_id,),
                commit=True
            )

            st.success(
                f"✅ Saved: {exercise} for {duration} mins. "
                f"{estimated_calories} kcal burned. Goal progress updated!"
            )
