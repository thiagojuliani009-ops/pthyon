from datetime import UTC, datetime
from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "data": datetime.now(UTC)},
    {"title": f"Criando uma aplicação com FastAPI", "data": datetime.now(UTC)}
]

@app.get("/posts")
def read_posts():  
    return fake_db

@app.get("/posts/{framework}")
def read_framework_posts(framework: str): 
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }

