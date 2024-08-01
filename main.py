from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr
from items_views import items_router
from users.views import users_router
import uvicorn

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/start_page')
def hello_index():
    return {'message': "Hello!"}


if __name__ == '__main__':
    uvicorn.run('app:main', reload=True)
