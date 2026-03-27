from contextlib import asynccontextmanager

import databases
import sqlalchemy as sa
from fastapi import FastAPI
from controllers import post



DATABASE_URL= "sqlite: ///./blog.db"

database = databases.Database(DATABASE_URL)
metadata = sa.metadata()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_routerr(post.router)

















