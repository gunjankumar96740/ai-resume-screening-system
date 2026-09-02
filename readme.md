# AI Resume Screening System

An AI-powered resume screening system that analyzes a candidate's resume against a job description and generates ATS scores, skill analysis, and interview questions.

## Features

- Upload resume in PDF format
- Extract text from resume
- Extract skills from resume and job description
- Calculate skill match score
- Generate ATS score
- Identify matched skills
- Identify missing skills
- Generate strengths and weaknesses
- Generate easy, medium, and hard interview questions
- REST API using FastAPI
- Interactive UI using Streamlit
- LLM analysis using Groq

## Tech Stack

- Python
- FastAPI
- Streamlit
- Groq LLM
- Pydantic
- PyPDF2
- REST API

## Project Structure

```text
app/
├── frontend.py
├── llm.py
├── main.py
├── parser.py
├── prompts.py
├── schemas.py
└── skills.py