import streamlit as st

from ui.styles import apply_styles
from ui.components import (
    show_header,
    show_score,
    show_skills,
    show_challenge,
)

from services.analyzer import analyze_resume
from services.question_generator import generate_questions

from coding.executor import execute_solution
from coding.evaluator import evaluate_solution
from coding.test_cases import DEFAULT_TEST_CASES


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="SkillBridge",
    page_icon="🚀",
    layout="wide",
)


# =====================================================
# CUSTOM STYLING
# =====================================================

apply_styles()


# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "resume" not in st.session_state:
    st.session_state.resume = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "questions" not in st.session_state:
    st.session_state.questions = None

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

if "coding_result" not in st.session_state:
    st.session_state.coding_result = None


# =====================================================
# FALLBACK ANALYSIS
# =====================================================

def fallback_analysis():
    return {
        "match_score": 72,
        "matched_skills": [
            "Python",
            "Git",
        ],
        "missing_skills": [
            "REST API",
            "Docker",
            "Testing",
        ],
        "strengths": [
            "Good Python foundation",
            "Basic software development experience",
        ],
        "weaknesses": [
            "Limited REST API experience",
            "Limited Docker experience",
        ],
        "skill_gaps": [
            "REST API",
            "Docker",
            "Testing",
        ],
        "recommendations": [
            "Practice building REST APIs with Python",
            "Learn Docker fundamentals",
            "Practice automated testing",
        ],
    }


# =====================================================
# FALLBACK QUESTIONS
# =====================================================

def fallback_questions():
    return {
        "questions": [
            {
                "question": (
                    "Write a Python function named solution(numbers) "
                    "that returns the sum of all numbers in a list."
                ),
                "skill": "Python",
                "difficulty": "Easy",
            },
            {
                "question": (
                    "Explain how a REST API works and describe "
                    "the difference between GET and POST requests."
                ),
                "skill": "REST API",
                "difficulty": "Medium",
            },
            {
                "question": (
                    "Explain how Docker containers help developers "
                    "maintain consistent application environments."
                ),
                "skill": "Docker",
                "difficulty": "Medium",
            },
        ]
    }


# =====================================================
# HOME PAGE
# =====================================================

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
        placeholder="Paste your job description here...",
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

            # =================================================
            # AI RESUME ANALYSIS
            # =================================================

            with st.spinner("🤖 AI is analyzing your skills..."):

                try:

                    analysis = analyze_resume(
                        resume,
                        job_description,
                    )

                    # Check whether AI returned usable data
                    if (
                        not isinstance(analysis, dict)
                        or "match_score" not in analysis
                    ):

                        st.warning(
                            "AI response was unavailable. "
                            "Using SkillBridge demo analysis."
                        )

                        analysis = fallback_analysis()

                except Exception as error:

                    st.warning(
                        "AI service is temporarily unavailable. "
                        "Using SkillBridge fallback analysis."
                    )

                    analysis = fallback_analysis()

                    print(
                        "Analyzer error:",
                        error,
                    )

            st.session_state.analysis = analysis

            # =================================================
            # GET SKILL GAPS
            # =================================================

            skill_gaps = analysis.get(
                "skill_gaps",
                analysis.get(
                    "missing_skills",
                    [],
                ),
            )

            # =================================================
            # AI QUESTION GENERATION
            # =================================================

            with st.spinner(
                "🧠 Generating your personalized assessment..."
            ):

                try:

                    questions = generate_questions(
                        skill_gaps
                    )

                    if (
                        not isinstance(questions, dict)
                        or "questions" not in questions
                        or not questions["questions"]
                    ):

                        questions = fallback_questions()

                except Exception as error:

                    print(
                        "Question generator error:",
                        error,
                    )

                    questions = fallback_questions()

            st.session_state.questions = questions

            st.session_state.page = "results"

            st.rerun()


# =====================================================
# RESULTS PAGE
# =====================================================

elif st.session_state.page == "results":

    show_header()

    st.markdown(
        "## 📊 Your Skill Gap Analysis"
    )

    analysis = st.session_state.analysis

    if not analysis:
        analysis = fallback_analysis()

    score = analysis.get(
        "match_score",
        0,
    )

    matched_skills = analysis.get(
        "matched_skills",
        [],
    )

    missing_skills = analysis.get(
        "missing_skills",
        [],
    )

    strengths = analysis.get(
        "strengths",
        [],
    )

    recommendations = analysis.get(
        "recommendations",
        [],
    )

    # =================================================
    # SCORE
    # =================================================

    show_score(score)

    st.divider()

    # =================================================
    # SKILLS
    # =================================================

    show_skills(
        matched_skills,
        missing_skills,
    )

    # =================================================
    # STRENGTHS
    # =================================================

    if strengths:

        st.markdown(
            "### 💪 Your Strengths"
        )

        for strength in strengths:

            st.write(
                f"✅ {strength}"
            )

    # =================================================
    # RECOMMENDATIONS
    # =================================================

    if recommendations:

        st.markdown(
            "### 💡 Recommendations"
        )

        for recommendation in recommendations:

            st.write(
                f"• {recommendation}"
            )

    st.divider()

    st.info(
        "🎯 SkillBridge has generated a personalized "
        "assessment based on your skill gaps."
    )

    # =================================================
    # START ASSESSMENT
    # =================================================

    if st.button(
        "🚀 Start Personalized Assessment",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.page = "assessment"

        st.rerun()

    # =================================================
    # NEW ANALYSIS
    # =================================================

    if st.button(
        "← Analyze Another Resume"
    ):

        st.session_state.analysis = None
        st.session_state.questions = None
        st.session_state.selected_question = None
        st.session_state.coding_result = None

        st.session_state.page = "home"

        st.rerun()


# =====================================================
# ASSESSMENT PAGE
# =====================================================

elif st.session_state.page == "assessment":

    show_header()

    st.markdown(
        "## 🧠 Personalized Coding Assessment"
    )

    questions_data = st.session_state.questions

    if not questions_data:
        questions_data = fallback_questions()

    questions = questions_data.get(
        "questions",
        [],
    )

    # =================================================
    # NO QUESTIONS
    # =================================================

    if not questions:

        st.error(
            "No assessment questions were generated."
        )

        if st.button(
            "← Back to Results"
        ):

            st.session_state.page = "results"

            st.rerun()

    else:

        # =================================================
        # QUESTION SELECTOR
        # =================================================

        question_numbers = list(
            range(
                1,
                len(questions) + 1,
            )
        )

        selected_number = st.selectbox(
            "Select Assessment Question",
            question_numbers,
        )

        selected_question = questions[
            selected_number - 1
        ]

        st.session_state.selected_question = (
            selected_question
        )

        # =================================================
        # CHALLENGE
        # =================================================

        challenge = {
            "title": (
                f"Question {selected_number}: "
                f"{selected_question.get(
                    'skill',
                    'Skill Assessment'
                )}"
            ),
            "description": selected_question.get(
                "question",
                "Complete the coding challenge.",
            ),
            "difficulty": selected_question.get(
                "difficulty",
                "Medium",
            ),
        }

        show_challenge(challenge)

        st.divider()

        # =================================================
        # CODING SECTION
        # =================================================

        st.markdown(
            "### 🧑‍💻 Write Your Python Solution"
        )

        code = st.text_area(
            "Python Code",
            value="""def solution(numbers):
    # Write your solution here
    return sum(numbers)
""",
            height=300,
        )

        col1, col2 = st.columns(2)

        # =================================================
        # RUN CODE
        # =================================================

        with col1:

            if st.button(
                "▶️ Run Code",
                type="primary",
                use_container_width=True,
            ):

                execution = execute_solution(code)

                # -----------------------------------------
                # EXECUTION ERROR
                # -----------------------------------------

                if not execution["success"]:

                    st.error(
                        f"❌ {execution['error']}"
                    )

                # -----------------------------------------
                # EVALUATE CODE
                # -----------------------------------------

                else:

                    result = evaluate_solution(
                        execution["solution"],
                        DEFAULT_TEST_CASES,
                    )

                    st.session_state.coding_result = (
                        result
                    )

                    st.success(
                        f"Score: {result['score']}%"
                    )

                    st.markdown(
                        f"**Passed:** "
                        f"{result['passed_tests']} / "
                        f"{result['total_tests']}"
                    )

                    # -------------------------------------
                    # TEST RESULTS
                    # -------------------------------------

                    for test in result["results"]:

                        if test["passed"]:

                            st.success(
                                f"Test {test['test_case']} "
                                f"— PASS"
                            )

                        else:

                            st.error(
                                f"Test {test['test_case']} "
                                f"— FAIL"
                            )

        # =================================================
        # BACK BUTTON
        # =================================================

        with col2:

            if st.button(
                "← Back to Results",
                use_container_width=True,
            ):

                st.session_state.page = "results"

                st.rerun()