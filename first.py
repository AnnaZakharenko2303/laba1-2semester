from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #создала экземпляр приложения

@app.get("/", response_class=HTMLResponse)#декоратор с маршрутом
async def read_root(): #функция вызывается при гет запросе 
    with open("first+.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
