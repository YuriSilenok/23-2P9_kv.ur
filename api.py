"""api для решение уравнения"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from main import kv_ur

app = FastAPI()


@app.get("/kvur/")
async def get_answer(a: float, b: float, c: float):
    """Получения ответа"""
    output = kv_ur(a, b, c)
    return output


@app.get("/", response_class=HTMLResponse)
async def page_output():
    """Вывод страницы"""
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
