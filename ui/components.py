import streamlit as st


def show_header():
    st.markdown(
        """
        <div class="hero">
            <h1>🚀 SkillBridge</h1>
            <p>AI-Powered Employability Gap Analyzer</p>
            <p>Find your skill gaps. Practice what matters.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_score(score):
    st.markdown(
        f"""
        <div class="score">
            {score}%
        </div>
        <p style="text-align:center;">Job Readiness Match</p>
        """,
        unsafe_allow_html=True,
    )


def show_skills(matched_skills, missing_skills):

    st.markdown(
        '<div class="section-title">✅ Matched Skills</div>',
        unsafe_allow_html=True,
    )

    if matched_skills:
        cols = st.columns(3)

        for index, skill in enumerate(matched_skills):
            cols[index % 3].success(skill)

    st.markdown(
        '<div class="section-title">⚠️ Skills to Improve</div>',
        unsafe_allow_html=True,
    )

    if missing_skills:
        cols = st.columns(3)

        for index, skill in enumerate(missing_skills):
            cols[index % 3].warning(skill)


def show_challenge(challenge):

    st.markdown(
        '<div class="section-title">💻 Personalized Coding Assessment</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="challenge-box">
            <h3>{challenge["title"]}</h3>
            <p>{challenge["description"]}</p>
            <b>Difficulty:</b> {challenge["difficulty"]}
        </div>
        """,
        unsafe_allow_html=True,
    )