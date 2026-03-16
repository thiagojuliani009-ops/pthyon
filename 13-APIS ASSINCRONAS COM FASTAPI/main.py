from datetime import UTC, datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/posts/{framework}")
def read_posts(framework: str):  # Adicione o parâmetro aqui
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }

