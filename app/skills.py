COMMON_SKILLS = [
    "python",
    "sql",
    "fastapi",
    "docker",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "power bi",
    "excel",
    "git",
    "langchain",
    "langgraph"
]
def extract_skills(text: str):

    text = text.lower()

    skills = []

    for skill in COMMON_SKILLS:

        if skill in text:
            skills.append(skill)

    return skills
def compare_skills(resume_skills,jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)
    matched = list(resume_set.intersection(jd_set))
    missing = list(jd_set - resume_set)
    return matched, missing
jd_skills = [
    "python",
    "sql",
    "fastapi",
    "docker",
    "aws"
]
matched_skills = [
    "python",
    "sql",
    "fastapi"
]
def calculate_match_score(matched_skills,jd_skills):

    if len(jd_skills) == 0:
        return 0

    score = (
        len(matched_skills)
        / len(jd_skills)
    ) * 100

    return round(score, 2)

    