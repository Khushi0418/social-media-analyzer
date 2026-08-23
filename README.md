# AI Social Media Content Analyzer

## Overview

AI Social Media Content Analyzer is a Streamlit-based web application that helps users evaluate and improve social media content. Users can upload PDF documents, image files, or manually enter captions for analysis.

The application extracts text from uploaded files and generates engagement insights, sentiment analysis, strengths, weaknesses, and AI-powered recommendations using Google Gemini.

---

## Features

### Document Upload
- Upload PDF files
- Upload image files (PNG, JPG, JPEG)

### Text Extraction
- PDF text extraction using PyMuPDF
- OCR-based image text extraction using Google Gemini Vision

### Content Analysis
- Engagement score calculation
- Sentiment analysis
- Hashtag detection
- CTA (Call-To-Action) detection
- Emoji detection
- Strength and weakness identification

### AI Recommendations
- Engagement reasoning
- Content strengths and weaknesses
- Improved caption suggestions
- Better hashtag recommendations
- CTA improvements
- Engagement optimization tips

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- TextBlob
- PyMuPDF
- Pillow

---

## Project Structure

```
social-media-analyzer/
│
├── app.py
├── analyzer.py
├── extractor.py
├── gemini_helper.py
├── requirements.txt
├── README.md
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/Khushi0418/social-media-content-analyzer.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment variable

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

4. Run the application

```bash
streamlit run app.py
```

---

## Deployment

The application is deployed using Streamlit Cloud.

---

## Author

Khushi Singh
B.Tech CSE, VIT Vellore