import streamlit as st
import requests
from backend.github_analyzer import analyze_repo
from backend.scorer import calculate_score
from backend.roadmap import generate_roadmap

st.set_page_config(
    page_title="GitGrade",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 GitGrade")
st.caption("AI-Powered GitHub Repository Analyzer")

repo_url = st.text_input(
    "Paste GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Analyze Repository"):
    if not repo_url.strip():
        st.warning("Please enter a valid GitHub repository URL.")
    else:
        with st.spinner("Analyzing repository..."):
            try:
                analysis = analyze_repo(repo_url)
                score, summary = calculate_score(analysis)
                roadmap = generate_roadmap(analysis)

                # ---- Score & Level ----
                st.metric("Score", f"{score} / 100")

                if score < 40:
                    level = "Beginner"
                elif score < 65:
                    level = "Intermediate"
                elif score < 85:
                    level = "Advanced"
                else:
                    level = "Excellent"

                st.info(f"Project Level: **{level}**")

                # ---- Summary ----
                st.subheader("🧠 AI Mentor Summary")
                st.write(summary)

                # ---- Roadmap ----
                st.subheader("🛣️ Personalized Roadmap")
                for item in roadmap:
                    st.markdown(f"- {item}")

                st.caption(
                    "⚠️ Scores are heuristic-based and intended for guidance, not absolute judgment."
                )

            except Exception as e:
                st.error("Failed to analyze repository. Please check the URL.")
