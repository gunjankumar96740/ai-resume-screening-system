
import streamlit as st
import requests
import pandas as pd

st.title("AI Resume Screening System")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Enter Job Description"
)

if st.button("Analyze Resume"):

    if resume is None or job_description == "":
        st.warning("Please upload resume and enter job description")

    else:

        files = {
            "file": (
                resume.name,
                resume,
                "application/pdf"
            )
        }

        data = {
            "job_description": job_description
        }

        response = requests.post(
            "https://ai-resume-screening-system-r5oo.onrender.com/analyze-resume",
            files=files,
            data=data
        )

        result = response.json()

        st.header("Analysis Result")

        st.write("### Candidate Name")
        st.write(result["candidate_name"])

        # Score Cards
        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Score", result["ats_score"])

        with col2:
            st.metric("Match Score", result["match_score"])

        # Visualization 1: Score Comparison
        st.divider()

        st.write("### Score Comparison")

        score_df = pd.DataFrame({
            "Metric": ["ATS Score", "Match Score"],
            "Score": [
                result["ats_score"],
                result["match_score"]
            ]
        })

        st.bar_chart(
            score_df,
            x="Metric",
            y="Score"
        )

        # Visualization 2: Skill Distribution
        st.write("### Skill Distribution")

        matched_count = len(result["matched_skills"])
        missing_count = len(result["missing_skills"])

        if matched_count + missing_count > 0:

            skill_df = pd.DataFrame({
                "Skill Type": ["Matched Skills", "Missing Skills"],
                "Count": [matched_count, missing_count]
            })

            st.bar_chart(
                skill_df,
                x="Skill Type",
                y="Count"
            )

            # Skill Coverage
            coverage = (
                matched_count /
                (matched_count + missing_count)
            ) * 100

            st.metric(
                "Skill Coverage",
                f"{coverage:.1f}%"
            )

        else:
            st.info("No skills available for visualization.")

        # Matched Skills
        st.write("### Matched Skills")

        for skill in result["matched_skills"]:
            st.write(f"✅ {skill}")

        # Missing Skills
        st.write("### Missing Skills")

        for skill in result["missing_skills"]:
            st.write(f"❌ {skill}")

        # Strengths
        st.write("### Strengths")

        for strength in result["strengths"]:
            st.write(f"• {strength}")

        # Weaknesses
        st.write("### Weaknesses")

        for weakness in result["weaknesses"]:
            st.write(f"• {weakness}")

        # Easy Questions
        st.write("### Easy Questions")

        for question in result["easy_questions"]:
            st.write(f"• {question}")

        # Medium Questions
        st.write("### Medium Questions")

        for question in result["medium_questions"]:
            st.write(f"• {question}")

        # Hard Questions
        st.write("### Hard Questions")

        for question in result["hard_questions"]:
            st.write(f"• {question}")
