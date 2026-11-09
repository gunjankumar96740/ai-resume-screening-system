import os
import json
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
from app.schemas import ResumeAnalysis
api_key=os.getenv("GROQ_API_KEY")
client=Groq(api_key=api_key)
def analyze_resume(prompt:str):
    response=client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
            'role':'user',
            'content':prompt
            }
        ],
        response_format={"type":"json_object"}
    )
    answer= response.choices[0].message.content
    data=json.loads(answer)
    analysis=ResumeAnalysis.model_validate(data)
    return analysis

def extract_skills_with_llm(resume_text, job_description):

    prompt = f"""
    You are an expert resume screening system.

    Compare the resume with the job description.

    RESUME:
    {resume_text[:12000]}

    JOB DESCRIPTION:
    {job_description[:8000]}

    Identify all relevant skills required by the job.

    Find which required skills are demonstrated in the resume.

    Consider equivalent skills only when supported by evidence.

    Do not invent skills or assume experience.

    Return only valid JSON:

    {{
        "matched_skills": [],
        "missing_skills": []
    }}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0
    )

    data = json.loads(
        response.choices[0].message.content
    )

    return data

