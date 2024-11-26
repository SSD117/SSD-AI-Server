from fastapi import FastAPI
from pydantic import BaseModel
from cluster import cluster

class Survey(BaseModel):
    preference: int
    intense: int
    frequency: int
    friend: int
    goal: int
    method: int
    activity: int
    place: int
    time: int
    type: int
app = FastAPI()

@app.post("/")
async def read_root(survey: Survey):
    survey_dict = survey.model_dump()
    user_scores = []
    for key, val in survey_dict.items():
        user_scores.append(val)
    result = cluster(user_scores)

    return {"sports": result}