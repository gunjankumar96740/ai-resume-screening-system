import streamlit as st
import requests

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
            "http://127.0.0.1:8000/analyze-resume",
            files=files,
            data=data
        )

        result = response.json()

        st.header("Analysis Result")

        st.write("### Candidate Name")
        st.write(result["candidate_name"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Score", result["ats_score"])

        with col2:
            st.metric("Match Score", result["match_score"])

        st.write("### Matched Skills")
        st.write(result["matched_skills"])

        st.write("### Missing Skills")
        st.write(result["missing_skills"])

        st.write("### Strengths")
        st.write(result["strengths"])

        st.write("### Weaknesses")
        st.write(result["weaknesses"])

        st.write("### Easy Questions")
        st.write(result["easy_questions"])

        st.write("### Medium Questions")
        st.write(result["medium_questions"])

        st.write("### Hard Questions")
        st.write(result["hard_questions"])