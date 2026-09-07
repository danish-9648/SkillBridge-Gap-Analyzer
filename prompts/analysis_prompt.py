def create_analysis_prompt(resume, job_description):

    prompt = f"""
You are an AI Employability Analyzer.

Analyze the candidate's resume against the given job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Identify:

1. Matching skills
2. Missing skills
3. Candidate strengths
4. Candidate weaknesses
5. Important skill gaps
6. Overall employability score from 0 to 100
7. Personalized recommendations

Return ONLY valid JSON in this format:

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "skill_gaps": [],
    "recommendations": []
}}
"""

    return prompt