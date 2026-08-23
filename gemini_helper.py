import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.6-flash")

def generate_ai_feedback(caption, platform):

    prompt = f"""
You are an expert social media strategist.

Analyze this caption:

{caption}

Provide:
1. Engagement reasoning
2. Strengths
3. Weaknesses
4. Improved caption
5. 15 hashtags
6. Better CTA
7. Tips to improve engagement

Format clearly.
"""

    response = model.generate_content(prompt)

    return response.text