import json

from services.llm_service import ask_llm
from prompts.coding_prompt import create_coding_prompt


def generate_questions(skill_gaps):

    prompt = create_coding_prompt(skill_gaps)

    response = ask_llm(prompt)

    try:
        questions = json.loads(response)
    except json.JSONDecodeError:
        questions = {
            "error": "LLM returned invalid JSON",
            "raw_response": response
        }

    return questions