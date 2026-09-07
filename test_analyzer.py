from services.analyzer import analyze_resume


resume = """
I know Python, Java, SQL and HTML.
I have created a student management project.
"""


job_description = """
We are looking for a software developer.

Required skills:
Python, SQL, React, Django and REST API.
"""


result = analyze_resume(
    resume,
    job_description
)

print(result)