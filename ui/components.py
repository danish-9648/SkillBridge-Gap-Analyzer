import streamlit as st


def show_header():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🚀</div>
            <h1>SkillBridge</h1>
            <p class="hero-subtitle">
                AI-Powered Employability Gap Analyzer
            </p>
            <p class="hero-description">
                Find your skill gaps. Practice what matters.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_score(score):
    st.markdown(
        f"""
        <div class="score-card">
            <div class="score">{score}%</div>
            <div class="score-label">Job Readiness Match</div>
            <div class="score-description">
                Your resume matches this job description by
                approximately {score}%.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_skills(matched_skills, missing_skills):

    st.markdown(
        """
        <div class="section-title">
            <span>✓</span> Matched Skills
        </div>
        """,
        unsafe_allow_html=True,
    )

    if matched_skills:

        cols = st.columns(2)

        for index, skill in enumerate(matched_skills):

            with cols[index % 2]:
                st.markdown(
                    f"""
                    <div class="skill-match">
                        ✓ &nbsp; {skill}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    else:

        st.info("No matching skills found yet.")

    st.markdown(
        """
        <div class="section-title">
            <span>⚠</span> Skills to Improve
        </div>
        """,
        unsafe_allow_html=True,
    )

    if missing_skills:

        cols = st.columns(2)

        for index, skill in enumerate(missing_skills):

            with cols[index % 2]:
                st.markdown(
                    f"""
                    <div class="skill-missing">
                        ⚠ &nbsp; {skill}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    else:

        st.success("Great! No major skill gaps found.")


def show_challenge(challenge):

    st.markdown(
        """
        <div class="section-title">
            💻 Personalized Coding Assessment
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="challenge-box">

            <div class="challenge-header">

                <div>
                    <h2>{challenge["title"]}</h2>
                </div>

                <span class="difficulty">
                    {challenge["difficulty"]}
                </span>

            </div>

            <div class="challenge-description">
                <strong>Problem Statement</strong>
                <p>{challenge["description"]}</p>
            </div>

            <div class="example-box">
                <strong>Example</strong>

                <p>
                    <b>Input:</b>
                    {challenge["example_input"]}
                </p>

                <p>
                    <b>Expected Output:</b>
                    {challenge["example_output"]}
                </p>
            </div>

            <div class="challenge-tip">
                💡 Write a function named
                <strong>solution(numbers)</strong>
                and return the expected result.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )