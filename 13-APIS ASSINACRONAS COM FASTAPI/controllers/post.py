from datetime import UTC, datetime
from typing import Annotated
from fastapi import APIRouter, status, Cookie, Header, Response
from shermas.post import PostIn 
from views.post import PostOut


router = APIRouter(prefix="/post")

fake_db = [
     {"title": "Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
     {"title": "Criando uma aplicação com Starlett", "data": datetime.now(UTC), "published": False},

]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post 

@router.get("/", response_model=list[PostOut])
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
    tail = skip = limit
    return [post for post in fake_db[skip : tail] if post["published"] is published ]

@router.get("/{framework}", reponse_model=PostOut)
def read_root(framework: str):
    return {
        "posts": [
            {"title":f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"title":f"Internacional uma app {framework}", "date": datetime.now(UTC)},
        ]
    }

