from services.skillbridge_service import run_skillbridge_analysis


resume = """
I know Python, Java, SQL and HTML.
I have created a student management project.
"""


job_description = """
We are looking for a software developer.

Required skills:
Python, SQL, React, Django and REST API.
"""


result = run_skillbridge_analysis(
    resume,
    job_description
)


print("\n===== FINAL SKILLBRIDGE RESULT =====")
print(result)