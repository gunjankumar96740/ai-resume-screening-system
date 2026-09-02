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
