# 🤖 AI Resume Screening System

An AI-powered resume screening system that analyzes a candidate's resume against a job description and generates ATS scores, skill matching, strengths, weaknesses, and interview questions.

## 🎯 Project Overview

Recruiters often need to screen many resumes against job descriptions.

This project automates the initial screening process by:

1. Accepting a resume in PDF format
2. Extracting resume text
3. Extracting skills from the resume and job description
4. Comparing candidate skills with required skills
5. Calculating a deterministic skill-match score
6. Sending resume and job-description information to an LLM
7. Generating ATS analysis and interview questions
8. Validating the LLM response using Pydantic
9. Displaying the results through a Streamlit interface

---

## ✨ Features

- 📄 PDF resume upload
- 📝 Job description input
- 🔍 Resume text extraction
- 🧠 Skill extraction
- 🔗 Skill matching
- 📊 Deterministic skill-match score
- 🤖 LLM-powered resume analysis
- 🎯 ATS score generation
- ✅ Matched skills identification
- ❌ Missing skills identification
- 💪 Strength analysis
- ⚠️ Weakness analysis
- 💬 Easy, medium, and hard interview questions
- 🚀 FastAPI REST API
- 🖥️ Streamlit frontend
- 🔐 Pydantic response validation

---

## 🏗️ System Architecture

```text
                    Resume PDF
                        │
                        ▼
                ┌─────────────────┐
                │    Streamlit    │
                │    Frontend     │
                └────────┬────────┘
                         │
                         │ HTTP Request
                         ▼
                ┌─────────────────┐
                │     FastAPI     │
                │      API        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   PDF Parser    │
                │    PyPDF2       │
                └────────┬────────┘
                         │
                         ▼
                   Resume Text
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Skill Extraction       ATS Prompt
              │                     │
              ▼                     ▼
       Skill Comparison        Groq LLM
              │                     │
              ▼                     ▼
        Match Score            JSON Output
                                    │
                                    ▼
                           Pydantic Validation
                                    │
                                    ▼
                            Final Analysis
                                    │
                                    ▼
                             Streamlit UI