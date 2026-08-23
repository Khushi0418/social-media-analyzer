def build_prompt(caption, metrics):

    return f"""
You are a professional social media strategist.

Caption:
{caption}

Metrics:
{metrics}

Generate:

1. Engagement Score Explanation
2. Strengths
3. Weaknesses
4. Improved Caption
5. 15 Hashtags
6. Better CTA
7. Engagement Tips

Format clearly.
"""