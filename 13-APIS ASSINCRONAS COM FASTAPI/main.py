from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers import post
from databases import database, engine, metadata # Importa do novo arquivo

# Cria as tabelas se não existirem
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
