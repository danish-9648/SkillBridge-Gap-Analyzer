import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        .main {
            padding-top: 2rem;
        }

        .hero {
            text-align: center;
            padding: 25px 10px;
        }

        .hero h1 {
            font-size: 42px;
            margin-bottom: 5px;
        }

        .hero p {
            font-size: 18px;
            color: #777;
        }

        .skill-card {
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #ddd;
            margin-bottom: 12px;
        }

        .score {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
        }

        .section-title {
            font-size: 26px;
            font-weight: 600;
            margin-top: 20px;
        }

        .challenge-box {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #ddd;
            margin: 15px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )