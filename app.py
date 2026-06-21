import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(
page_title="Student Performance Prediction",
page_icon="🎓",
layout="wide"
)

model = joblib.load("model.pkl")

st.markdown("""
<h1 style='text-align:center;color:#4F46E5;'>
🎓 Student Performance Prediction System
</h1>

<h4 style='text-align:center;color:gray;'>
AI Powered Academic Analytics Dashboard
</h4>
""", unsafe_allow_html=True)

st.markdown("---")
st.sidebar.title("🎓 Student Dashboard")

st.sidebar.markdown("---")

st.sidebar.write("Enter student details below")
study_hours = st.sidebar.slider("Study Hours", 0, 15, 5)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 80)
assignments = st.sidebar.slider("Assignments Completed", 0, 10, 5)
previous_marks = st.sidebar.slider("Previous Marks", 0, 100, 70)
st.subheader("📋 Student Profile")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
    **Study Hours:** {study_hours}

    **Attendance:** {attendance}%

    """)

with col2:
    st.info(f"""
    **Assignments:** {assignments}

    **Previous Marks:** {previous_marks}

    """)
prediction = model.predict([
[study_hours, attendance, assignments, previous_marks]
])[0]

if prediction >= 85:
    level = "Excellent"
elif prediction >= 70:
    level = "Good"
elif prediction >= 50:
    level = "Average"
else:
    level = "At Risk"
if prediction >= 85:
    level = "Excellent"
elif prediction >= 70:
    level = "Good"
elif prediction >= 50:
    level = "Average"
else:
    level = "At Risk"

# PASTE HERE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

st.subheader("🎯 Performance Gauge")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=float(prediction),
    title={"text": "Predicted Marks"},
    gauge={
        "axis": {"range": [0, 100]},
        "steps": [
            {"range": [0, 50], "color": "red"},
            {"range": [50, 70], "color": "orange"},
            {"range": [70, 85], "color": "yellow"},
            {"range": [85, 100], "color": "green"}
        ]
    }
))

st.plotly_chart(fig, use_container_width=True)

# YOUR EXISTING CODE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

col1, col2, col3 = st.columns(3)

with col1:
    ...
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🎯 Predicted Marks",
        f"{prediction:.2f}"
    )

with col2:
    st.metric(
        "📅 Attendance",
        f"{attendance}%"
    )

with col3:
    st.metric(
        "🏆 Performance",
        level
    )
    st.subheader("🤖 AI Recommendations")

if attendance < 75:
    st.error("Attendance is low. Aim for 75% or above.")

if study_hours < 4:
    st.warning("Increase study time to at least 5 hours daily.")

if assignments < 5:
    st.warning("Complete more assignments regularly.")

if prediction >= 85:
    st.success("Excellent performance predicted! Keep it up.")

elif prediction >= 70:
    st.info("Good performance. A little more effort can improve marks.")

else:
    st.error("Performance risk detected. Improve attendance and study hours.")
    st.subheader("📈 Performance Score")

score = min(max(prediction / 100, 0), 1)

st.progress(score)

st.write(f"Performance Score: {prediction:.2f}/100")
st.subheader("📊 Student Performance Analysis")

chart_data = pd.DataFrame({
    "Factor": [
        "Study Hours",
        "Attendance",
        "Assignments",
        "Previous Marks"
    ],
    "Value": [
        study_hours,
        attendance,
        assignments,
        previous_marks
    ]
})

fig = px.bar(
    chart_data,
    x="Factor",
    y="Value",
    title="Performance Indicators"
)

st.plotly_chart(fig, use_container_width=True)
df = pd.DataFrame({
"Feature": [
"Study Hours",
"Attendance",
"Assignments",
"Previous Marks"
],
"Value": [
study_hours,
attendance,
assignments,
previous_marks
]
})
fig = px.bar(df, x="Feature", y="Value")
st.plotly_chart(fig, use_container_width=True)
st.subheader("🥧 Performance Distribution")

pie_data = pd.DataFrame({
    "Category": [
        "Study Hours",
        "Attendance",
        "Assignments",
        "Previous Marks"
    ],
    "Value": [
        study_hours,
        attendance,
        assignments,
        previous_marks
    ]
})

fig_pie = px.pie(
    pie_data,
    names="Category",
    values="Value",
    hole=0.4
)

st.plotly_chart(fig_pie, use_container_width=True)
st.progress(attendance / 100)

if attendance < 75:
    st.warning("Increase attendance above 75%.")

if study_hours < 4:
    st.warning("Study at least 5-6 hours daily.")
if prediction >= 85:
    st.success("Excellent performance predicted.")
report = f"""
STUDENT PERFORMANCE REPORT

Predicted Marks : {prediction:.2f}
Performance     : {level}

Study Hours     : {study_hours}
Attendance      : {attendance}%
Assignments     : {assignments}
Previous Marks  : {previous_marks}

Generated by:
Student Performance Prediction System
"""

st.download_button(
    label="📄 Download Report",
    data=report,
    file_name="student_report.txt",
    mime="text/plain"
)