import streamlit as st

from analyzer import analyze_caption
from gemini_helper import generate_ai_feedback

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

caption = st.text_area(
    "Enter Caption",
    height=200
)

if st.button("Analyze"):

    result = analyze_caption(caption)

    st.metric(
        "Engagement Score",
        f"{result['score']}/10"
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