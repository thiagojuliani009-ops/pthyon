from datetime import UTC, datetime
from typing import Annotated

from fastapi import Response, Cookie, Header, status, APIRouter
from schemas.post import PostIn
from views.post import PostOut


router = APIRouter(prefix="/post")

fake_db = [
    {"title": "Criando uma aplicação com Django", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com FastAPI", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "data": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com starlett", "data": datetime.now(UTC), "published": False},
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

    response.set_cookie(key="user", value="thiagojuliani009@gmail.com")

    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")

    tail = skip + limit

    return [post for post in fake_db[skip:tail] if post["published"] is published]





@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str): 
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now(UTC)}
        ]
    }
from fastapi import APIRouter
from schemas.post import PostIn # O nome aqui deve ser igual ao do arquivo acima
from models.post import posts
from main import database

router = APIRouter()

@router.post("/posts/", response_model=PostIn)
async def create_post(post: PostIn):
    query = posts.insert().values(title=post.title, content=post.content, published=post.published)
    last_record_id = await database.execute(query)
    return {**post.dict(), "id": last_record_id}
