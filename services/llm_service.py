import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()


# Models are tried in this order.
# 3.7 is the primary model.
# 3.6 and 3.5 are fallback models.
MODELS = [
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
]


def ask_llm(prompt):

    api_key = os.environ.get("GEMINI_API_KEY")

    print("API key detected:", bool(api_key))

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set."
        )

    client = genai.Client(
        api_key=api_key
    )

    last_error = None

    for index, model in enumerate(MODELS):

        try:

            print(
                f"Calling Gemini model: {model}"
            )

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                }
            )

            if not response.text:

                raise ValueError(
                    "Gemini returned an empty response."
                )

            print(
                f"Gemini response received from {model}"
            )

            return response.text

        except Exception as error:

            last_error = error

            print(
                f"Gemini model {model} failed: {error}"
            )

            # Don't wait after the final model.
            if index < len(MODELS) - 1:
                print("Trying next Gemini model...")
                time.sleep(1)

    raise RuntimeError(
        f"All Gemini models failed. Last error: {last_error}"
    )