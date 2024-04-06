from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
app = FastAPI()

class userRequest(BaseModel):
    text: str
    canditate_labels: List[str]


class userResponse(BaseModel):
    label: str
    score: str





