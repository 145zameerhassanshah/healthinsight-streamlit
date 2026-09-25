# 🏥 HealthInsight

**Healthcare Analytics & AI Learning Platform**

HealthInsight is a progressive Streamlit project developed during my AI Internship. Instead of creating separate applications for every task, new Streamlit, Python, data analytics, and AI concepts are gradually integrated into one healthcare-themed application.

> **Educational Notice:** HealthInsight is for learning and demonstration only. It does not provide medical diagnosis, treatment recommendations, or clinical decision support.

---

## 🎯 Project Objective

The goal is to learn concepts practically and gradually develop a portfolio-ready application.

```text
Streamlit Fundamentals
        ↓
Layout & Navigation
        ↓
Interactive Widgets
        ↓
Risk Score Calculator
        ↓
Data & Visualization
        ↓
Machine Learning
```

---

## 🛠 Technology Stack

* Python
* Streamlit
* VS Code
* Python Virtual Environment
* Git
* GitHub
* PowerShell

Pandas is now used for structured patient and visit data. Future stages may introduce NumPy, Matplotlib, Plotly, and Scikit-learn.
---

## 🚀 Run the Application

Create and activate the environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install Streamlit:

```powershell
python -m pip install streamlit
```

Run HealthInsight:

```powershell
streamlit run app.py
```

---

##  Streamlit Foundation

The first stage introduced Streamlit fundamentals, including:

* `st.set_page_config()`
* `st.title()`
* `st.header()`
* `st.subheader()`
* `st.write()`
* `st.text()`
* `st.markdown()`
* `st.caption()`
* `st.info()`
* `st.success()`
* `st.warning()`
* `st.error()`

This stage also introduced Streamlit's top-to-bottom script execution and rerun model.

---

## 🧭 Layout & Navigation

HealthInsight was extended with:

* `st.sidebar`
* Sidebar navigation
* `st.selectbox()`
* Conditional page rendering
* Multiple application sections

Current navigation includes:

* Home
* Risk Score Calculator
* Patient Information
* Healthcare Analytics
* AI / ML
* Datasets
* About

---

## 🩺 Demo Risk Score Calculator

The latest stage explores Streamlit layouts, buttons, sliders, and text inputs.

Implemented components:

* `st.container()` for grouping inputs
* `st.columns()` for two-column layout
* `st.slider()` for age
* `st.slider()` for systolic blood pressure
* `st.slider()` for glucose level
* `st.selectbox()` for gender
* `st.text_input()` for optional reference ID
* `st.button()` for calculation
* `st.metric()` for displaying the result

The calculator uses simple Python conditional logic to generate an educational demo score from `0–100`.

Gender is included as an interactive input but is not assigned arbitrary medical risk points.

> The score is a programming demonstration and is not a clinically validated risk assessment.


## 📊 Clinical Metrics Tables & Trend Charts

HealthInsight was extended with an interactive Clinical Metrics Dashboard using synthetic patient data.

### Implemented Features

- Pandas for structured healthcare data
- `pd.DataFrame()` for patient and visit records
- `st.dataframe()` for an interactive patient metrics table
- Age, systolic blood pressure, glucose, and readmission risk score
- Multiple visit records for each patient
- `st.selectbox()` for patient selection
- Pandas Boolean filtering for selected patient data
- `st.line_chart()` for blood pressure trend visualization
- Dynamic chart updates when the selected patient changes

### Data Flow

```text
Synthetic Patient Data
        ↓
Pandas DataFrame
        ↓
Clinical Metrics Table
        ↓
Select Patient
        ↓
Filter Visit History
        ↓
Blood Pressure Trend Chart
---

## 🧪 Testing

The application was tested locally with multiple input values.

Example:

```text
Age:             40
Blood Pressure:  120
Glucose:         100

Demo Risk Score: 15/100
```

Required screenshots of the calculator and its output were also captured for internship submission.

---

## 🌿 Git Workflow

Development follows a feature-based workflow:

```text
main
 ├── feature/streamlit-foundation
 ├── feature/layout-navigation
 ├── feature/risk-score-calculator
 └── feature/clinical-metrics-trends
```

Workflow:

```text
Feature Branch → Development → Testing
→ Documentation → Commit → Push
→ Pull Request → Merge
```

---



## 🔮 Future Direction

HealthInsight will continue to evolve according to upcoming internship tasks.

Planned areas include forms, validation, file uploads, Session State,
advanced visualization, machine learning, model evaluation, caching,
and application optimization.

The objective is to keep **learning, implementing, testing, documenting, and integrating** each concept into the same evolving project.
