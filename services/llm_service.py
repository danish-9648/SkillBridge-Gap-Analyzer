import os
import time
from google import genai


def ask_llm(prompt):

    api_key = os.environ.get("GEMINI_API_KEY")

    print("API key detected:", bool(api_key))

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    max_retries = 3

    for attempt in range(max_retries):

        try:
            print(f"Calling Gemini... Attempt {attempt + 1}")

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            if not response.text:
                raise ValueError("Gemini returned an empty response.")

            return response.text

        except Exception as e:

            print(f"Gemini request failed: {e}")

            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)

            else:
                raise