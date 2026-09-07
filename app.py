import streamlit as st

st.set_page_config(
    page_title="SkillBridge",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 SkillBridge")

st.subheader(
    "Employability Gap Analyzer & Coding Assessment Engine"
)

st.write(
    "Discover your skill gaps and prove your skills "
    "through a personalized coding challenge."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area(
        "📄 Your Resume",
        height=300,
        placeholder="Paste your resume here..."
    )

with col2:
    job_description = st.text_area(
        "💼 Job Description",
        height=300,
        placeholder="Paste the job description here..."
    )

if st.button("🔍 Analyze Skill Gap", type="primary"):

    if not resume.strip():
        st.warning("Please enter your resume.")

    elif not job_description.strip():
        st.warning("Please enter the job description.")

    else:
        st.success("Resume and Job Description received!")

        st.header("💻 Coding Challenge")

        st.info(
            "Coding engine integration will be loaded here."
        )