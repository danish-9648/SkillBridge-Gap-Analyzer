import json

from services.llm_service import ask_llm
from prompts.analysis_prompt import create_analysis_prompt


def analyze_resume(resume, job_description):

    prompt = create_analysis_prompt(
        resume,
        job_description
    )

    response = ask_llm(prompt)

    try:
        analysis = json.loads(response)
    except json.JSONDecodeError:
        analysis = {
            "error": "LLM returned invalid JSON",
            "raw_response": response
        }

    return analysis