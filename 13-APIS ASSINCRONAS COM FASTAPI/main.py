from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers import post
import sqlalchemy as sa
import databases

# 1. Configuração do Banco de Dados (Corrigido)
DATABASE_URL = "sqlite:///./blog.db"
database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

engine = sa.create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

# 2. Gerenciador de Ciclo de Vida (Lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

# 3. Inicialização do App (O que faltava)
app = FastAPI(lifespan=lifespan)

# 4. Inclusão das Rotas
app.include_router(post.router)
