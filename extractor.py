import fitz
from PIL import Image
import google.generativeai as genai


def extract_pdf_text(file):
    pdf = fitz.open(
        stream=file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    return text


def extract_image_text(file):

    image = Image.open(file)

    model = genai.GenerativeModel(
        "models/gemini-3.6-flash"
    )

    response = model.generate_content([
        "Extract all text from this image exactly as written.",
        image
    ])

    return response.text