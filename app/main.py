
from fastapi import FastAPI, UploadFile, File, Form
import os
import shutil

from app.parser import extract_text
from app.prompts import ATS_PROMPT
from app.llm import analyze_resume, extract_skills_with_llm
from app.schemas import ResumeAnalysis

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(
    title="AI Resume Screening API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Resume Screening API"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/upload-resume")
@app.post(
    "/analyze-resume",
    response_model=ResumeAnalysis
)
async def upload_resume_api(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_text(file_path)

    # Dynamic skill extraction using Groq LLM
    skill_analysis = extract_skills_with_llm(
        resume_text,
        job_description
    )

    matched_skills = skill_analysis["matched_skills"]
    missing_skills = skill_analysis["missing_skills"]

    # Calculate match score using Python
    total_skills = len(set(matched_skills + missing_skills))

    if total_skills == 0:
        match_score = 0
    else:
        match_score = round(
            len(set(matched_skills)) / total_skills * 100,
            2
        )

    # Create ATS prompt
    prompt = ATS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )

    # Existing LLM resume analysis
    result = analyze_resume(prompt)

    # Update structured response
    result.match_score = match_score
    result.matched_skills = matched_skills
    result.missing_skills = missing_skills

    print(result)

    return result
