from datetime import UTC, datetime
from typing import Annotated

from fastapi import Cookie, FastAPI, status
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com starlett", "data": datetime.now(UTC), "published": False},
]

class Post (BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def  create_post(post: Post):
    fake_db.append(post.model_dump())
    return post
    

@app.get("/posts/")
def read_posts(published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None):
    # Filter the list first
    filtered_posts = [post for post in fake_db if post["published"] is published]

    # O print precisa estar aqui dentro (com recuo/identação)
    print(f"cookie: {ads_id}")

    # Then apply the slice for pagination
    return filtered_posts[skip : skip + limit]

@app.get("/posts/{framework}")
def read_framework_posts(framework: str): 
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }

