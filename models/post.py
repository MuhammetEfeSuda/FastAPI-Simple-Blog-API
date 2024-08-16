from pydantic import BaseModel
from typing import List
from datetime import datetime

class Post(BaseModel):
    title: str
    short_description: str
    description: str
    tags: List[str]


class Postcreate(Post):
    create_date: datetime = None


class Postupdate(Post):
    update_date: datetime = None