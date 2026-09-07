from services.question_generator import generate_questions


skill_gaps = [
    "React",
    "Django",
    "REST API"
]


result = generate_questions(skill_gaps)

print(result)