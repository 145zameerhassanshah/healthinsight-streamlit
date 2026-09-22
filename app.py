import streamlit as st


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="HealthInsight",
    page_icon="🏥",
    layout="wide"
)


# --------------------------------------------------
# Application Header
# --------------------------------------------------

st.title("🏥 HealthInsight")
st.header("Healthcare Risk & Analytics Platform")

st.write(
    "Welcome to HealthInsight, an educational healthcare "
    "analytics application built with Python and Streamlit."
)


# --------------------------------------------------
# About the Application
# --------------------------------------------------

st.subheader("About HealthInsight")

st.markdown("""
HealthInsight is a learning-focused healthcare analytics platform
designed to demonstrate how Python, data analytics, and artificial
intelligence can be combined in a web application.

### Planned Learning Modules

- 👤 Patient Information
- 📊 Healthcare Data Analytics
- 📈 Interactive Data Visualization
- 🤖 Machine-Learning Risk Prediction
- 📁 Dataset Exploration
- 📋 Model Performance Analysis
""")


# --------------------------------------------------
# Healthcare Data & AI Workflow
# --------------------------------------------------

st.header("Healthcare Data & AI Workflow")

st.markdown("""
**HealthInsight learning workflow:**

`Data → Cleaning → Analysis → Visualization → Machine Learning → Results`
""")


# --------------------------------------------------
# Current Learning Stage
# --------------------------------------------------

st.subheader("Current Learning Stage")

st.write(
    "In this first stage, we are learning the Streamlit framework, "
    "its basic execution model, and static content rendering."
)


# --------------------------------------------------
# System Status
# --------------------------------------------------

st.header("System Status")

st.success("Streamlit foundation initialized successfully.")

st.info(
    "No patient data or machine-learning model is being processed "
    "in this foundation stage."
)

st.warning(
    "This project is intended for educational and demonstration "
    "purposes only."
)


# --------------------------------------------------
# Educational Notice
# --------------------------------------------------

st.divider()

st.markdown("""
> **Educational Notice:**  
> HealthInsight is a learning and demonstration project. It does
> not provide medical diagnosis, treatment recommendations, or
> clinical decision-making.
""")


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.caption("Built with Python + Streamlit")