import re
from textblob import TextBlob

def analyze_caption(text):

    words = len(text.split())

    hashtags = len(re.findall(r"#\w+", text))

    emojis = len(
        re.findall(
            r"[\U0001F600-\U0001F64F]",
            text
        )
    )

    question = "?" in text

    cta_words = [
        "download",
        "join",
        "buy",
        "click",
        "signup",
        "try"
    ]

    cta = any(
        word in text.lower()
        for word in cta_words
    )

    score = 0

    if words >= 20:
        score += 2

    if hashtags >= 3:
        score += 2

    if emojis >= 1:
        score += 1

    if question:
        score += 2

    if cta:
        score += 3

    strengths = []

    if cta:
        strengths.append("Contains a strong call-to-action")

    if hashtags >= 3:
        strengths.append("Good hashtag usage")

    if words >= 20:
        strengths.append("Detailed content")

    weaknesses = []

    if not question:
        weaknesses.append("No engagement question")

    if hashtags < 3:
        weaknesses.append("Too few hashtags")

    if emojis == 0:
        weaknesses.append("No emojis used")
    sentiment = TextBlob(text).sentiment.polarity
    return {
        "score": score,
        "words": words,
        "hashtags": hashtags,
        "emojis": emojis,
        "cta": cta,
        "strengths": strengths,
        "weaknesses": weaknesses
    }