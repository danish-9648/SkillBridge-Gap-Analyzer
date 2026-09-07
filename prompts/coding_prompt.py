def create_coding_prompt(skill_gaps):

    prompt = f"""
You are an AI coding assessment generator for an employability platform.

The candidate has the following skill gaps:

{skill_gaps}

Generate personalized coding/practical questions to assess these missing skills.

Requirements:

1. Generate 3 questions.
2. Questions should be suitable for a college-level computer science student.
3. Focus mainly on the identified skill gaps.
4. Mix conceptual and practical coding questions.
5. Do not provide the answers.
6. Assign a difficulty level: Easy, Medium, or Hard.

Return ONLY valid JSON in this format:

{{
    "questions": [
        {{
            "question": "Question text",
            "skill": "Related skill",
            "difficulty": "Easy"
        }}
    ]
}}
"""

    return prompt