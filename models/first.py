from fastapi import FastAPI
from models import User

app = FastAPI()
user = User(name="Anna Zakharenko", id=1)#кземпляр класса юзер

@app.get("/users")
async def get_user():
    return user 
