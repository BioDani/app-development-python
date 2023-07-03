from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str
    age: int
    score: float
    date: datetime
    
    