import streamlit as st

from coding.executor import execute_solution

from ui.styles import apply_styles
from ui.components import (
    show_header,
    show_score,
    show_skills,
    show_challenge,
)


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="SkillBridge",
    page_icon="🚀",
    layout="wide",
)


# Apply custom styling
apply_styles()


# ---------------- SESSION STATE ----------------

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
        """
        <div style="text-align:center; margin-bottom:25px;">
            <h2>🎯 Compare Your Resume With Your Dream Job</h2>
            <p style="color:#777;">
                Discover your skill gaps and get a personalized coding challenge.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Resume and Job Description side by side
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📄 Your Resume")

        resume = st.text_area(
            "Resume",
            placeholder=(
                "Paste your resume text here...\n\n"
                "Example:\n"
                "• Python\n"
                "• JavaScript\n"
                "• React\n"
                "• Git"
            ),
            height=300,
            label_visibility="collapsed",
        )

    with col2:

        st.markdown("### 💼 Job Description")

        job_description = st.text_area(
            "Job Description",
            placeholder=(
                "Paste the job description here...\n\n"
                "Example:\n"
                "Looking for a Python developer with "
                "REST API, Docker and testing skills..."
            ),
            height=300,
            label_visibility="collapsed",
        )

    st.markdown("")

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

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:20px;">
            <h2>📊 Your Skill Gap Analysis</h2>
            <p style="color:#777;">
                Here's how your profile matches the job requirements.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    st.markdown(
        """
        <div style="text-align:center; margin:15px 0 25px 0;">
            <h3>💡 What This Means</h3>
            <p style="color:#777;">
                You have a solid foundation for this role.
                Strengthening the missing skills below can improve
                your job readiness.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_skills(
        matched_skills,
        missing_skills,
    )

    st.divider()

    st.markdown(
        """
        <div class="recommendation-box">
            <h3>🎯 Recommended Next Step</h3>
            <p>
                Your personalized assessment will focus on one
                of the skills you need to improve.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "🚀 Start Personalized Assessment",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.page = "assessment"

        st.rerun()

    if st.button(
        "← Analyze Another Resume"
    ):

        st.session_state.page = "home"

        st.rerun()


# ---------------- ASSESSMENT PAGE ----------------

elif st.session_state.page == "assessment":

    show_header()

    challenge = {
        "title": "Sort a List of Numbers",
        "description": (
            "Create a Python function that takes a list "
            "of numbers and returns the numbers in "
            "ascending order."
        ),
        "difficulty": "Easy",
        "example_input": "[3, 1, 2]",
        "example_output": "[1, 2, 3]",
    }

    show_challenge(challenge)

    st.markdown("### 🧑‍💻 Write Your Solution")

    code = st.text_area(
        "Python Code",
        value="""def solution(numbers):
    # Write your solution here
    return sorted(numbers)
""",
        height=300,
    )

    col1, col2 = st.columns(2)


    # ---------------- RUN CODE ----------------

    with col1:

        if st.button(
            "▶️ Run Code",
            type="primary",
            use_container_width=True,
        ):

            result = execute_solution(code)

            if not result["success"]:

                st.error(result["error"])

            else:

                try:

                    test_input = [3, 1, 2]

                    output = result["solution"](test_input)

                    st.success(
                        "✅ Code executed successfully!"
                    )

                    st.write(
                        "Test Input:",
                        test_input,
                    )

                    st.write(
                        "Your Output:",
                        output,
                    )

                except Exception as error:

                    st.error(
                        f"Runtime Error: {error}"
                    )


    # ---------------- BACK BUTTON ----------------

    with col2:

        if st.button(
            "← Back to Results",
            use_container_width=True,
        ):

            st.session_state.page = "results"

            st.rerun()