from PIL import Image
import pytesseract
import pdfplumber
import streamlit as st

from analyzer import analyze_caption
from gemini_helper import generate_ai_feedback, extract_image_text
from extractor import extract_pdf_text
st.set_page_config(
    page_title="AI Social Media Analyzer",
    page_icon="📈",
    layout="wide"
)


st.title("AI Social Media Analyzer")

platform = st.selectbox(
    "Select Platform",
    ["Instagram", "LinkedIn", "Twitter/X", "Facebook"]
)

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

caption = st.text_area(
    "Or Enter Caption",
    height=200
)
if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":

        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        caption = text

    else:

        caption = extract_image_text(uploaded_file)

    st.success("Text extracted successfully!")

    st.text_area(
        "Extracted Text",
        caption,
        height=200
    )

if st.button("Analyze"):

    result = analyze_caption(caption)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Score",
            f"{result['score']}/10"
        )

    with col2:
        st.metric(
            "Words",
            result["words"]
        )

    with col3:
        st.metric(
            "Hashtags",
            result["hashtags"]
        )

    with col4:
        st.metric(
            "Sentiment",
            result["sentiment"]
        )

    st.subheader("📊 Analysis Results")

    st.write(f"**Words:** {result['words']}")
    st.write(f"**Hashtags:** {result['hashtags']}")
    st.write(f"**Emojis:** {result['emojis']}")
    st.write(f"**CTA Present:** {result['cta']}")       
    st.subheader("✅ Strengths")

    for item in result["strengths"]:
        st.success(item)

    st.subheader("⚠️ Weaknesses")

    for item in result["weaknesses"]:
        st.warning(item)
    st.subheader("🤖 AI Recommendations")

    with st.spinner("Analyzing content..."):

        ai_result = generate_ai_feedback(
            caption,
            platform
        )

    tab1, tab2 = st.tabs([
        "📊 AI Analysis",
        "🤖 Full Report"
    ])

    with tab1:
        st.write("Platform:", platform)
        st.write("Score:", result["score"])
        st.metric(
            "Sentiment",
            result["sentiment"]
        )

    with tab2:
        st.markdown(ai_result)
    st.download_button(
    label="📥 Download AI Report",
    data=ai_result,
    file_name="analysis_report.txt",
    mime="text/plain"
    )