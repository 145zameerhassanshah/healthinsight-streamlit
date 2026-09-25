import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="HealthInsight",
    page_icon="🏥",
    layout="wide"
)


# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------

st.sidebar.title("🏥 HealthInsight")

st.sidebar.caption("Healthcare Analytics & AI Learning Platform")

page = st.sidebar.selectbox(
    "Navigate to",
    [
        "Home",
            "Risk Score Calculator",

        "Patient Information",
        "Healthcare Analytics",
        "AI / ML",
        "Datasets",
        "About"
    ]
)


# --------------------------------------------------
# Main Application
# --------------------------------------------------

st.title("🏥 HealthInsight")
st.header("Healthcare Risk & Analytics Platform")

st.write(
    "Welcome to HealthInsight, an educational healthcare "
    "analytics application built with Python and Streamlit."
)


# --------------------------------------------------
# Current Page
# --------------------------------------------------

st.subheader(f"Current Section: {page}")

if page == "Home":

    st.markdown("""
    ### Welcome to HealthInsight

    HealthInsight is a learning-focused healthcare analytics
    platform designed to demonstrate Python, data analytics,
    visualization, and artificial intelligence concepts.
    """)

    st.info(
        "Select a section from the sidebar to explore the platform."
    )

elif page == "Risk Score Calculator":

    st.markdown("""
    ### 🩺 Demo Risk Score Calculator

    Adjust the values below and calculate a simple educational
    risk score based on the selected inputs.
    """)

    st.warning(
        "Educational demonstration only. This calculator is not "
        "a validated medical or clinical risk assessment."
    )

    # ----------------------------------------------
    # Input Container
    # ----------------------------------------------

    with st.container():

        st.subheader("Health Inputs")

        # Optional text input to practice st.text_input()
        reference_id = st.text_input(
            "Reference ID (Optional)",
            placeholder="Example: DEMO-001"
        )

        # Create two columns
        col1, col2 = st.columns(2)

        # ------------------------------------------
        # Left Column
        # ------------------------------------------

        with col1:

            age = st.slider(
                "Age",
                min_value=18,
                max_value=100,
                value=40,
                step=1
            )

            glucose = st.slider(
                "Glucose Level (mg/dL)",
                min_value=50,
                max_value=300,
                value=100,
                step=1
            )

        # ------------------------------------------
        # Right Column
        # ------------------------------------------

        with col2:

            blood_pressure = st.slider(
                "Systolic Blood Pressure (mmHg)",
                min_value=70,
                max_value=200,
                value=120,
                step=1
            )

            gender = st.selectbox(
                "Gender",
                [
                    "Female",
                    "Male",
                    "Other / Prefer not to say"
                ]
            )

    st.divider()

    # ----------------------------------------------
    # Calculate Button
    # ----------------------------------------------

    if st.button(
        "Calculate Demo Risk Score",
        type="primary"
    ):

        risk_score = 0

        # Age score
        if age >= 60:
            risk_score += 25
        elif age >= 45:
            risk_score += 15
        elif age >= 30:
            risk_score += 5

        # Blood pressure score
        if blood_pressure >= 160:
            risk_score += 25
        elif blood_pressure >= 140:
            risk_score += 15
        elif blood_pressure >= 120:
            risk_score += 5

        # Glucose score
        if glucose >= 200:
            risk_score += 30
        elif glucose >= 140:
            risk_score += 20
        elif glucose >= 100:
            risk_score += 5

        # Ensure score never exceeds 100
        risk_score = min(risk_score, 100)

        # ------------------------------------------
        # Results
        # ------------------------------------------

        st.subheader("Risk Score Result")

        st.metric(
            "Demo Risk Score",
            f"{risk_score}/100"
        )

        if risk_score < 25:
            st.success("Demo Category: Lower Score Range")

        elif risk_score < 50:
            st.info("Demo Category: Moderate Score Range")

        else:
            st.warning("Demo Category: Higher Score Range")

        if reference_id:
            st.caption(f"Reference ID: {reference_id}")

        st.caption(
            f"Selected gender: {gender}. Gender is displayed as "
            "an input but is not used in this demonstration formula."
        )

        st.error(
            "This educational score must not be used for diagnosis, "
            "treatment, or clinical decision-making."
        )

elif page == "Patient Information":

    st.markdown("""
    ### Patient Information

    This section will later contain structured patient information
    and healthcare-related data.
    """)

    st.warning(
        "Patient data functionality will be added in a later stage."
    )


elif page == "Healthcare Analytics":

    st.markdown("""
    ### 📊 Clinical Metrics Dashboard

    Explore synthetic patient metrics and analyze vital-sign
    trends across multiple visits.
    """)

    st.info(
        "This dashboard uses synthetic data for educational "
        "and demonstration purposes only."
    )

    # --------------------------------------------------
    # Patient Summary Data
    # --------------------------------------------------

    patient_data = {
        "Patient ID": ["P001", "P002", "P003", "P004", "P005"],
        "Age": [34, 47, 58, 66, 72],
        "Systolic BP (mmHg)": [118, 126, 138, 145, 160],
        "Glucose (mg/dL)": [92, 105, 128, 151, 185],
        "Readmission Risk Score": [10, 20, 35, 60, 75]
    }

    patient_df = pd.DataFrame(patient_data)

    # --------------------------------------------------
    # Clinical Metrics Table
    # --------------------------------------------------

    st.subheader("Patient Clinical Metrics")

    st.dataframe(
        patient_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------
    # Patient Visit History
    # --------------------------------------------------

    st.subheader("Patient Vital Sign Trend")

    visit_data = {
        "Patient ID": [
            "P001", "P001", "P001", "P001", "P001",
            "P002", "P002", "P002", "P002", "P002",
            "P003", "P003", "P003", "P003", "P003",
            "P004", "P004", "P004", "P004", "P004",
            "P005", "P005", "P005", "P005", "P005"
        ],

        "Visit": [
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5,
            1, 2, 3, 4, 5
        ],

        "Systolic BP (mmHg)": [
            116, 120, 118, 122, 118,
            124, 128, 126, 130, 126,
            132, 135, 140, 136, 138,
            138, 142, 147, 144, 145,
            150, 155, 158, 162, 160
        ]
    }

    visit_df = pd.DataFrame(visit_data)

    # --------------------------------------------------
    # Patient Selection
    # --------------------------------------------------

    selected_patient = st.selectbox(
        "Select Patient",
        patient_df["Patient ID"].tolist()
    )

    # --------------------------------------------------
    # Filter Selected Patient
    # --------------------------------------------------

    patient_trend = visit_df[
        visit_df["Patient ID"] == selected_patient
    ]

    st.caption(
        f"Showing systolic blood pressure trend for {selected_patient}"
    )

    # --------------------------------------------------
    # Blood Pressure Trend Chart
    # --------------------------------------------------

    st.line_chart(
        patient_trend,
        x="Visit",
        y="Systolic BP (mmHg)"
    )
    
elif page == "AI / ML":

    st.markdown("""
    ### Artificial Intelligence & Machine Learning

    This section will eventually contain educational machine-learning
    workflows and model predictions.
    """)

    st.info(
        "Machine-learning functionality will be introduced later."
    )


elif page == "Datasets":

    st.markdown("""
    ### Dataset Explorer

    This section will eventually allow healthcare datasets
    to be explored and analyzed.
    """)

    st.info(
        "Dataset functionality will be added in a later stage."
    )


elif page == "About":

    st.markdown("""
    ### About HealthInsight

    HealthInsight is an educational project for learning how
    Python and Streamlit can be used to build healthcare
    analytics and AI applications.
    """)

    st.caption("Built with Python + Streamlit")