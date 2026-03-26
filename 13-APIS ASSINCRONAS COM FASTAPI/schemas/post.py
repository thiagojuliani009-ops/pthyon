from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostIn(BaseModel):
    title: str
    content: str
    published: bool = False
    published_at: Optional[datetime] = None