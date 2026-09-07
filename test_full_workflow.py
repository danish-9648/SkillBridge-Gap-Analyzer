from services.analyzer import analyze_resume
from services.question_generator import generate_questions


resume = """
I know Python, Java, SQL and HTML.
I have created a student management project.
"""


job_description = """
We are looking for a software developer.

Required skills:
Python, SQL, React, Django and REST API.
"""


# Step 1: Analyze resume
print("\n===== EMPLOYABILITY ANALYSIS =====")

analysis = analyze_resume(
    resume,
    job_description
)

print(analysis)


# Step 2: Get skill gaps
print("\n===== RAW ANALYSIS =====")
print(analysis)

skill_gaps = analysis.get("skill_gaps", [])

print("\n===== IDENTIFIED SKILL GAPS =====")
print(skill_gaps)


# Step 3: Generate questions from skill gaps
if skill_gaps:

    print("\n===== PERSONALIZED CODING QUESTIONS =====")

    questions = generate_questions(skill_gaps)

    print(questions)

else:

    print("No skill gaps found.")