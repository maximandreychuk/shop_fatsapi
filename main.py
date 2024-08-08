from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr
from items_views import items_router
from users.views import users_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:  # load db before launch app
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/start_page')
def hello_index():
    return {'message': "Hello!"}


if __name__ == '__main__':
    uvicorn.run('app:main', reload=True)
