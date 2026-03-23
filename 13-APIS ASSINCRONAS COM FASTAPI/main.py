from datetime import UTC, datetime
from typing import Annotated

from fastapi import Response, Cookie, FastAPI, status, Header
from pydantic import BaseModel

app = FastAPI()

# Banco de dados fake
fake_db = [
    {"title": "Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com starlett", "data": datetime.now(UTC), "published": False},
]

# Modelo de dados
class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False

# Rota para criar posts
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post

# Rota para ler posts com Filtro, Cookie e Header
@app.get("/posts/")
def read_posts(
    response: Response,
    published: bool = True, # Definido como True por padrão para evitar erro na URL
    limit: int = 10,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    # 1. Filtra a lista
    filtered_posts = [post for post in fake_db if post["published"] == published]

    # 2. Configura o cookie na resposta (aparece no navegador)
    response.set_cookie(key="user", value="thiagijuliani009.com")

    # 3. Prints de debug (aparecem no seu TERMINAL)
    if user_agent:
        print(f"Request coming from: {user_agent}")
    
    print(f"Cookie received: {ads_id}")

    # 4. Retorno final com fatiamento para paginação
    return filtered_posts[skip : skip + limit]

# Rota dinâmica por framework
@app.get("/posts/{framework}")
def read_framework_posts(framework: str): 
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }

