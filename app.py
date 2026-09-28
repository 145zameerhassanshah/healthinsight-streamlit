import streamlit as st
import pandas as pd


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="HealthInsight",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# SESSION STATE
# ==================================================

if "risk_threshold" not in st.session_state:
    st.session_state.risk_threshold = 0

if "selected_patient" not in st.session_state:
    st.session_state.selected_patient = "P001"


def reset_filters():
    st.session_state.risk_threshold = 0
    st.session_state.selected_patient = "P001"


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .dashboard-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.2);
        background-color: rgba(128,128,128,0.04);
    }

    .sidebar-footer {
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(128,128,128,0.2);
        font-size: 0.8rem;
        color: #777;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🏥 HealthInsight")

st.sidebar.caption(
    "Healthcare Analytics & AI Learning Platform"
)

st.sidebar.divider()

page = st.sidebar.selectbox(
    "Navigate",
    [
        "Home",
        "Risk Score Calculator",
        "Healthcare Analytics",
        "Patient Information",
        "AI / ML",
        "Datasets",
        "About"
    ]
)

st.sidebar.divider()

st.sidebar.markdown(
    """
    **Platform Modules**

    🏠 Overview  
    🩺 Risk Calculator  
    📊 Clinical Dashboard  
    👤 Patient Information  
    🤖 AI / ML  
    📁 Datasets  
    ℹ️ About
    """
)

st.sidebar.markdown(
    """
    <div class="sidebar-footer">
    Educational demonstration only.<br>
    Uses synthetic healthcare data.
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# MAIN HEADER
# ==================================================

st.markdown(
    '<div class="main-title">🏥 HealthInsight</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Healthcare Risk & Analytics Platform'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# HOME
# ==================================================

if page == "Home":

    st.header("Welcome to HealthInsight")

    st.write(
        """
        HealthInsight is a learning-focused healthcare analytics
        platform built with Python and Streamlit.

        The project progressively combines Streamlit interfaces,
        healthcare data processing, visualization, and future
        machine-learning concepts.
        """
    )

    st.info(
        "Select a module from the sidebar to explore the platform."
    )

    st.subheader("Learning Pipeline")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("1", "Data")

    with col2:
        st.metric("2", "Cleaning")

    with col3:
        st.metric("3", "Analysis")

    with col4:
        st.metric("4", "Visualization")

    with col5:
        st.metric("5", "Machine Learning")


# ==================================================
# RISK SCORE CALCULATOR
# ==================================================

elif page == "Risk Score Calculator":

    st.header("🩺 Demo Risk Score Calculator")

    st.write(
        """
        Adjust the health inputs below and calculate a simple
        educational demonstration score.
        """
    )

    st.warning(
        "This is an educational programming demonstration. "
        "It is not a validated medical or clinical risk assessment."
    )

    with st.container():

        st.subheader("Health Inputs")

        reference_id = st.text_input(
            "Reference ID (Optional)",
            placeholder="Example: DEMO-001"
        )

        col1, col2 = st.columns(2)

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

    if st.button(
        "Calculate Demo Risk Score",
        type="primary"
    ):

        risk_score = 0

        # Age
        if age >= 60:
            risk_score += 25

        elif age >= 45:
            risk_score += 15

        elif age >= 30:
            risk_score += 5

        # Blood pressure
        if blood_pressure >= 160:
            risk_score += 25

        elif blood_pressure >= 140:
            risk_score += 15

        elif blood_pressure >= 120:
            risk_score += 5

        # Glucose
        if glucose >= 200:
            risk_score += 30

        elif glucose >= 140:
            risk_score += 20

        elif glucose >= 100:
            risk_score += 5

        risk_score = min(risk_score, 100)

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
            st.caption(
                f"Reference ID: {reference_id}"
            )

        st.caption(
            f"Selected gender: {gender}. "
            "Gender is displayed as an input but is not "
            "used in this demonstration formula."
        )

        st.error(
            "This educational score must not be used for "
            "diagnosis, treatment, or clinical decision-making."
        )


# ==================================================
# HEALTHCARE ANALYTICS
# ==================================================

elif page == "Healthcare Analytics":

    st.header("📊 Clinical Metrics Dashboard")

    st.write(
        """
        Upload a healthcare CSV file to explore patient summaries,
        risk levels, patient details, and vital-sign trends.
        """
    )

    st.info(
        "This dashboard is designed for educational use "
        "with synthetic healthcare data."
    )

    # --------------------------------------------------
    # CSV UPLOAD
    # --------------------------------------------------

    st.subheader("📁 Upload Healthcare Dataset")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"],
        help=(
            "Upload a CSV containing patient visit records. "
            "The dataset should include patient identifiers, "
            "vital signs, dates, and risk scores."
        )
    )

    if uploaded_file is None:

        st.info(
            "Please upload a healthcare CSV file to activate "
            "the clinical dashboard."
        )

        st.markdown(
            """
            **Required columns**

            - Patient ID
            - Visit
            - Date
            - Age
            - Gender
            - Systolic BP (mmHg)
            - Diastolic BP (mmHg)
            - Glucose (mg/dL)
            - Readmission Risk Score
            """
        )

        st.stop()

    # --------------------------------------------------
    # READ CSV
    # --------------------------------------------------

    try:

        df = pd.read_csv(uploaded_file)

    except Exception as error:

        st.error(
            f"Unable to read the uploaded CSV: {error}"
        )

        st.stop()

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------

    required_columns = [
        "Patient ID",
        "Visit",
        "Date",
        "Age",
        "Gender",
        "Systolic BP (mmHg)",
        "Diastolic BP (mmHg)",
        "Glucose (mg/dL)",
        "Readmission Risk Score"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:

        st.error(
            "The uploaded CSV is missing required columns: "
            + ", ".join(missing_columns)
        )

        st.stop()

    # --------------------------------------------------
    # DATA CLEANING
    # --------------------------------------------------

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    numeric_columns = [
        "Visit",
        "Age",
        "Systolic BP (mmHg)",
        "Diastolic BP (mmHg)",
        "Glucose (mg/dL)",
        "Readmission Risk Score"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df = df.dropna(
        subset=required_columns
    )

    df = df.sort_values(
        ["Patient ID", "Date"]
    )

    if df.empty:

        st.error(
            "No valid records remain after data validation."
        )

        st.stop()

    st.success(
        f"Dataset loaded successfully: {len(df)} valid visit records."
    )

    # --------------------------------------------------
    # OVERVIEW CARDS
    # --------------------------------------------------

    st.divider()

    st.subheader("📌 Dataset Overview")

    card1, card2, card3, card4 = st.columns(4)

    with card1:

        st.metric(
            "👥 Patients",
            df["Patient ID"].nunique()
        )

    with card2:

        st.metric(
            "🗂 Visits",
            len(df)
        )

    with card3:

        st.metric(
            "🎂 Average Age",
            f"{df['Age'].mean():.1f}"
        )

    with card4:

        st.metric(
            "⚠️ Average Risk",
            f"{df['Readmission Risk Score'].mean():.1f}"
        )

    # --------------------------------------------------
    # FILTERS
    # --------------------------------------------------

    st.divider()

    st.subheader("🔎 Dashboard Filters")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:

        risk_filter = st.selectbox(
            "Risk Level",
            [
                "All",
                "Lower",
                "Moderate",
                "Higher"
            ]
        )

    # Create risk categories
    df["Risk Level"] = pd.cut(
        df["Readmission Risk Score"],
        bins=[-1, 24, 49, 100],
        labels=[
            "Lower",
            "Moderate",
            "Higher"
        ]
    )

    filtered_df = df.copy()

    if risk_filter != "All":

        filtered_df = filtered_df[
            filtered_df["Risk Level"] == risk_filter
        ]

    # --------------------------------------------------
    # PATIENT SELECTOR
    # --------------------------------------------------

    patient_options = filtered_df[
        "Patient ID"
    ].drop_duplicates().tolist()

    if not patient_options:

        st.warning(
            "No patients match the selected risk filter."
        )

        st.stop()

    with filter_col2:

        selected_patient = st.selectbox(
            "Select Patient",
            patient_options,
            key="selected_patient"
        )

    # --------------------------------------------------
    # FILTERED TABLE
    # --------------------------------------------------

    st.divider()

    st.subheader("👥 Patient Summary")

    summary_columns = [
        "Patient ID",
        "Age",
        "Gender",
        "Systolic BP (mmHg)",
        "Glucose (mg/dL)",
        "Readmission Risk Score",
        "Risk Level"
    ]

    patient_summary = (
        filtered_df[summary_columns]
        .drop_duplicates(subset=["Patient ID"])
        .sort_values("Patient ID")
    )

    st.dataframe(
        patient_summary,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # SELECTED PATIENT DATA
    # --------------------------------------------------

    patient_df = df[
        df["Patient ID"] == selected_patient
    ].sort_values("Date")

    if patient_df.empty:

        st.warning(
            "No visit data available for the selected patient."
        )

        st.stop()

    latest_record = patient_df.iloc[-1]

    # --------------------------------------------------
    # PATIENT DETAILS
    # --------------------------------------------------

    st.divider()

    st.subheader(
        f"👤 Patient Details — {selected_patient}"
    )

    detail1, detail2, detail3, detail4 = st.columns(4)

    with detail1:

        st.metric(
            "Age",
            int(latest_record["Age"])
        )

    with detail2:

        st.metric(
            "Gender",
            latest_record["Gender"]
        )

    with detail3:

        st.metric(
            "Latest Systolic BP",
            f"{latest_record['Systolic BP (mmHg)']:.0f} mmHg"
        )

    with detail4:

        st.metric(
            "Demo Risk Score",
            f"{latest_record['Readmission Risk Score']:.0f}"
        )

    # --------------------------------------------------
    # VITAL SIGN VISUALIZATION
    # --------------------------------------------------

    st.divider()

    st.subheader("📈 Vital Sign Trends")

    chart_type = st.selectbox(
        "Select Vital Sign",
        [
            "Systolic BP (mmHg)",
            "Diastolic BP (mmHg)",
            "Glucose (mg/dL)"
        ]
    )

    chart_data = patient_df[
        ["Date", chart_type]
    ].copy()

    chart_data = chart_data.set_index("Date")

    st.line_chart(
        chart_data,
        use_container_width=True
    )

    st.caption(
        f"Showing {chart_type} trend for {selected_patient} "
        "across recorded visits."
    )

    # --------------------------------------------------
    # VISIT HISTORY
    # --------------------------------------------------

    st.divider()

    st.subheader("📋 Visit History")

    visit_columns = [
        "Visit",
        "Date",
        "Systolic BP (mmHg)",
        "Diastolic BP (mmHg)",
        "Glucose (mg/dL)",
        "Readmission Risk Score"
    ]

    st.dataframe(
        patient_df[visit_columns],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # RESET
    # --------------------------------------------------

    st.divider()

    st.button(
        "🔄 Reset Dashboard Filters",
        on_click=reset_filters
    )

    st.caption(
        "HealthInsight uses synthetic data for educational "
        "demonstration and does not provide clinical advice."
    )


# ==================================================
# PATIENT INFORMATION
# ==================================================

elif page == "Patient Information":

    st.header("👤 Patient Information")

    st.write(
        """
        This section will eventually provide structured
        patient information and additional healthcare data.
        """
    )

    st.warning(
        "Advanced patient information functionality "
        "will be introduced in future stages."
    )


# ==================================================
# AI / ML
# ==================================================

elif page == "AI / ML":

    st.header("🤖 Artificial Intelligence & Machine Learning")

    st.write(
        """
        This section will eventually contain educational
        machine-learning workflows, model predictions,
        and model evaluation.
        """
    )

    st.info(
        "Machine-learning functionality will be introduced later."
    )


# ==================================================
# DATASETS
# ==================================================

elif page == "Datasets":

    st.header("📁 Dataset Explorer")

    st.write(
        """
        This section will eventually provide tools for
        exploring, validating, and preparing healthcare datasets.
        """
    )

    st.info(
        "Dataset exploration functionality will be expanded later."
    )


# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.header("ℹ️ About HealthInsight")

    st.write(
        """
        HealthInsight is an educational healthcare analytics
        and AI learning project developed with Python and Streamlit.

        The application is progressively extended as new
        programming, data analytics, visualization, and
        machine-learning concepts are learned.
        """
    )

    st.divider()

    st.subheader("Educational Notice")

    st.warning(
        "HealthInsight is not a medical diagnostic system "
        "and should not be used for treatment or clinical "
        "decision-making."
    )

    st.caption(
        "Built with Python + Streamlit"
    )