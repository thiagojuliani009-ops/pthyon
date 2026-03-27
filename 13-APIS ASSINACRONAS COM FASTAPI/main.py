from datetime import UTC, datetime
from typing import Annotated
from fastapi import FastAPI, status, Cookie, Header, Response
from pydantic import BaseModel

app = FastAPI()

fake_db = [
     {"title": "Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com Starlett", "data": datetime.now(UTC), "published": False},

]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post 

@app.get("/posts/")
def read_posts(
    response: Response,
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None, 
    user_agent: Annotated[str | None, Header()] = None,
    ):

    response.set_cookie(key="user", value="thiagojuliani@gmail.com")
    print(f"Cookie: {ads_id}")
    print(f"user-agent: {user_agent}")
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]



@app.get("/posts/{framework}")
def read_root(framework: str):
    return {
        "posts": [
            {"title":f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"title":f"Internacional uma app {framework}", "date": datetime.now(UTC)},
        ]
    }
