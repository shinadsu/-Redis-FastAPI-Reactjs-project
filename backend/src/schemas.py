from src.config import redis_db
from redis_om import HashModel
from typing import Optional


class Task(HashModel):
    name: str
    complete: Optional[bool] = 0
    
    class Meta: 
        database = redis_db