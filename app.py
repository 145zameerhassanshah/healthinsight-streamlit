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
# Sidebar Navigation
# --------------------------------------------------

st.sidebar.title("🏥 HealthInsight")

st.sidebar.caption("Healthcare Analytics & AI Learning Platform")

page = st.sidebar.selectbox(
    "Navigate to",
    [
        "Home",
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
    ### Healthcare Analytics

    This section will later contain healthcare data analysis,
    statistics, and visualizations.
    """)

    st.info(
        "Analytics functionality will be developed in future tasks."
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