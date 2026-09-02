from pydantic import BaseModel,Field
class ResumeAnalysis(BaseModel):
    candidate_name:str
    match_score:float=Field(ge=0,le=100)
    ats_score:float=Field(gt=0,le=100)
    strengths:list[str]
    weaknesses:list[str]
    matched_skills: list[str]
    missing_skills:list[str]
    easy_questions: list[str]
    medium_questions: list[str]
    hard_questions: list[str]