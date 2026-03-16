from datetime import UTC, datetime
from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
    {"title": f"Criando uma aplicação com starlett", "data": datetime.now(UTC), "published": True},
]

@app.get("/posts")
def read_posts(skip: int = 0, limit = len (fake_db), published: bool = True):   
    return [ post for post in fake_db[skip: skip + limit] if post["published"] is published]

@app.get("/posts/{framework}")
def read_framework_posts(framework: str): 
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }

