import streamlit as st
import pandas as pd
from db import query_db
import plotly.express as px

def show_dashboard(user_id):
    st.header("📊 Dashboard")

    # Fetch workout data including exercise
    workouts = query_db("SELECT date, exercise, calories_burned FROM workouts WHERE user_id=%s", (user_id,))
    if workouts:
        df = pd.DataFrame(workouts)
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

        # Bar chart: Calories burned over time
        st.subheader("🔥 Calories Burned Over Time")
        bar_chart = px.bar(
            df,
            x="date",
            y="calories_burned",
            title="Calories Burned by Date",
            labels={"date": "Date", "calories_burned": "Calories Burned"}
        )
        st.plotly_chart(bar_chart, use_container_width=True)

        # Bar chart: Calories burned by workout type
        st.subheader("💪 Calories Burned by Exercise Type")
        exercise_summary = df.groupby("exercise", as_index=False)["calories_burned"].sum()
        exercise_chart = px.bar(
            exercise_summary,
            x="exercise",
            y="calories_burned",
            title="Total Calories Burned per Exercise",
            labels={"exercise": "Exercise", "calories_burned": "Calories Burned"},
            color="calories_burned",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(exercise_chart, use_container_width=True)
    else:
        st.info("No workouts found.")

    # Goal Progress
    goals = query_db("SELECT goal_type, current_value, target_value FROM goals WHERE user_id=%s", (user_id,))
    if goals:
        st.subheader("🎯 Goal Progress")
        df_goals = pd.DataFrame(goals)
        df_goals["progress"] = (df_goals["current_value"] / df_goals["target_value"]) * 100
        df_goals["progress"] = df_goals["progress"].clip(upper=100)

        goal_chart = px.bar(
            df_goals,
            x="goal_type",
            y="progress",
            text="progress",
            labels={"goal_type": "Goal", "progress": "Progress (%)"},
            title="Goal Completion Progress"
        )
        goal_chart.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        goal_chart.update_layout(yaxis=dict(range=[0, 110]))
        st.plotly_chart(goal_chart, use_container_width=True)
    else:
        st.info("No goals set yet.")
