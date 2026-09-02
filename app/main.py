from fastapi import FastAPI,UploadFile,File,HTTPException
import os 
import shutil# copies file content efficiently
from app.parser import extract_text
from app.prompts import ATS_PROMPT
from app.llm import analyze_resume
from fastapi import Form
from app.skills import extract_skills,compare_skills,calculate_match_score
from app.schemas import ResumeAnalysis

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)

app=FastAPI(
    title="AI Resume Screening API",
    version="1.0.0"
)

@app.get("/")
def root():
    return{"message":"Welcome to AI Resume Screening API"
        }

@app.get("/health")
def health():
    return{"status":"healthy"}

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

    # Skill extraction
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # Skill comparison
    matched_skills, missing_skills = compare_skills(
        resume_skills,
        jd_skills
    )

    # Calculate score
    match_score = calculate_match_score(
        matched_skills,
        jd_skills
    )

    # Create prompt
    prompt = ATS_PROMPT.format(
        resume_text=resume_text,
        job_description=job_description
    )

    # LLM analysis
    result = analyze_resume(prompt)

    # Override with deterministic values
    result.match_score = match_score
    result.matched_skills = matched_skills
    result.missing_skills = missing_skills
    print(result)

    return result

