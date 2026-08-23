import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.6-flash")

def generate_ai_feedback(caption, platform):
    try:
        print("Gemini function started")

        model = genai.GenerativeModel(
            "models/gemini-3.6-flash"
        )

        print("Model created")

        prompt = f"""
Analyze the following {platform} social media caption.

Caption:
{caption}

Provide:

1. Engagement Reasoning
2. Strengths
3. Weaknesses
4. Improved Caption
5. Better Hashtags
6. Better CTA
7. Tips to Maximize Engagement

Be detailed and actionable.
"""

        response = model.generate_content(
            prompt,
            request_options={"timeout": 20}
        )

        print("Response received")

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return f"Gemini Error: {e}"