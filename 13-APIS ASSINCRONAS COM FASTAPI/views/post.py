from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostOut(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = False
    published_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        