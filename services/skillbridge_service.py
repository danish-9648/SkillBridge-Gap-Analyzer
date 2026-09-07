from services.analyzer import analyze_resume
from services.question_generator import generate_questions


def run_skillbridge_analysis(resume, job_description):

    # Analyze resume against job description
    analysis = analyze_resume(
        resume,
        job_description
    )

    # Extract skill gaps
    skill_gaps = analysis.get("skill_gaps", [])

    # Generate coding questions
    questions = []

    if skill_gaps:
        questions = generate_questions(skill_gaps)

    # Return complete result
    return {
        "analysis": analysis,
        "skill_gaps": skill_gaps,
        "coding_questions": questions
    }