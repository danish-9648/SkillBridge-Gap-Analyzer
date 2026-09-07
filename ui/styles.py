import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        /* ---------------- GENERAL ---------------- */

        .main {
            padding-top: 2rem;
        }


        /* ---------------- HERO ---------------- */

        .hero {
            text-align: center;
            padding: 25px 10px 35px 10px;
        }

        .hero-icon {
            font-size: 42px;
            margin-bottom: 5px;
        }

        .hero h1 {
            font-size: 44px;
            font-weight: 700;
            margin: 0;
        }

        .hero-subtitle {
            font-size: 20px;
            font-weight: 500;
            margin-top: 8px;
            margin-bottom: 3px;
        }

        .hero-description {
            font-size: 16px;
            color: #777;
            margin-top: 4px;
        }


        /* ---------------- SCORE ---------------- */

        .score-card {
            text-align: center;
            padding: 25px;
            border-radius: 16px;
            border: 1px solid #ddd;
            margin: 20px auto;
            max-width: 500px;
        }

        .score {
            font-size: 52px;
            font-weight: 700;
        }

        .score-label {
            font-size: 20px;
            font-weight: 600;
            margin-top: 5px;
        }

        .score-description {
            font-size: 14px;
            color: #777;
            margin-top: 8px;
        }


        /* ---------------- SECTION TITLES ---------------- */

        .section-title {
            font-size: 25px;
            font-weight: 650;
            margin-top: 25px;
            margin-bottom: 15px;
        }


        /* ---------------- SKILLS ---------------- */

        .skill-match {
            padding: 12px 15px;
            border-radius: 10px;
            border: 1px solid #b7dfc4;
            margin-bottom: 10px;
            font-weight: 500;
        }

        .skill-missing {
            padding: 12px 15px;
            border-radius: 10px;
            border: 1px solid #f0c36d;
            margin-bottom: 10px;
            font-weight: 500;
        }


        /* ---------------- CHALLENGE ---------------- */

        .challenge-box {
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #ddd;
            margin: 15px 0 25px 0;
        }

        .challenge-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
        }

        .challenge-header h2 {
            margin: 0;
        }

        .difficulty {
            padding: 6px 12px;
            border-radius: 20px;
            border: 1px solid #ccc;
            font-size: 14px;
            font-weight: 600;
        }

        .challenge-description {
            font-size: 16px;
            line-height: 1.6;
            margin-top: 15px;
        }

        .challenge-tip {
            margin-top: 20px;
            padding: 12px;
            border-radius: 10px;
            border: 1px dashed #bbb;
            font-size: 14px;
        }
        .recommendation-box {
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #aaa;
    margin: 20px 0;
    text-align: center;
}

.recommendation-box h3 {
    margin-bottom: 8px;
}

.recommendation-box p {
    color: #777;
    margin: 0;
}
        </style>
        """,
        unsafe_allow_html=True,
    )