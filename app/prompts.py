ATS_PROMPT = """
You are an expert Applicant Tracking System (ATS).

Compare the candidate's resume with the job description.

Calculate scores from 0 to 100.

match_score:
How closely the candidate's skills and experience match the
requirements of the job description.

ats_score:
How well the resume is structured and contains relevant
keywords for the job description.

Identify:
- skills present in both the resume and job description
- required skills missing from the resume
- candidate strengths
- candidate weaknesses
- relevant interview questions

Return ONLY valid JSON.

Required fields:
candidate_name
match_score
ats_score
matched_skills
strengths
weaknesses
missing_skills
easy_questions
medium_questions
hard_questions

Resume:
{resume_text}

Job Description:
{job_description}
"""