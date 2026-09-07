import streamlit as st

<<<<<<< HEAD
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
=======
from ui.styles import apply_styles
from ui.components import (
    show_header,
    show_score,
    show_skills,
    show_challenge,
)


# Page configuration
st.set_page_config(
    page_title="SkillBridge",
    page_icon="🚀",
    layout="wide",
)


# Apply custom styling
apply_styles()


# Session state
if "page" not in st.session_state:
    st.session_state.page = "home"


if "resume" not in st.session_state:
    st.session_state.resume = ""


if "job_description" not in st.session_state:
    st.session_state.job_description = ""


# ---------------- HOME PAGE ----------------

if st.session_state.page == "home":

    show_header()

    st.markdown(
        "### 🎯 Compare your resume with your dream job"
    )

    resume = st.text_area(
        "📄 Your Resume",
        placeholder="Paste your resume text here...",
        height=250,
    )

    job_description = st.text_area(
        "💼 Job Description",
        placeholder="Paste the job description here...",
        height=250,
    )

    if st.button(
        "🔍 Analyze My Skills",
        type="primary",
        use_container_width=True,
    ):

        if not resume.strip() or not job_description.strip():

            st.warning(
                "Please provide both your resume and the job description."
            )

        else:

            st.session_state.resume = resume
            st.session_state.job_description = job_description

            st.session_state.page = "results"

            st.rerun()


# ---------------- RESULTS PAGE ----------------

elif st.session_state.page == "results":

    show_header()

    st.markdown("## 📊 Your Skill Gap Analysis")

    # Temporary demo data.
    # Disha's AI logic will replace this later.

    score = 72

    matched_skills = [
        "Python",
        "JavaScript",
        "React",
        "Git",
    ]

    missing_skills = [
        "REST API",
        "Docker",
        "Testing",
    ]

    show_score(score)

    st.divider()

    show_skills(
        matched_skills,
        missing_skills,
    )

    st.divider()

    st.info(
        "💡 Your personalized assessment will focus "
        "on one of the skills you need to improve."
    )

    if st.button(
        "🚀 Start Personalized Assessment",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.page = "assessment"

        st.rerun()

    if st.button("← Analyze Another Resume"):

        st.session_state.page = "home"

        st.rerun()


# ---------------- ASSESSMENT PAGE ----------------

elif st.session_state.page == "assessment":

    show_header()

    challenge = {
        "title": "REST API Challenge",
        "description": (
            "Create a Python function that processes "
            "a list of API response objects and returns "
            "only the successful responses."
        ),
        "difficulty": "Easy",
    }

    show_challenge(challenge)

    st.markdown("### 🧑‍💻 Write Your Solution")

    code = st.text_area(
        "Python Code",
        value="""def solve(data):
    # Write your solution here
    pass
""",
        height=300,
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "▶️ Run Code",
            type="primary",
            use_container_width=True,
        ):

            st.info(
                "Code execution will be connected "
                "to the Pyodide coding engine."
            )

    with col2:

        if st.button(
            "← Back to Results",
            use_container_width=True,
        ):

            st.session_state.page = "results"

            st.rerun()
>>>>>>> feature/ancha-ui
