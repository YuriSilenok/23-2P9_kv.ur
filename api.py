"""api для решение уравнения"""
from fastapi import FastAPI
from main import kv_ur
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/kvur/")
async def get_answer(a: float, b: float, c: float):
    """Получения ответа"""
    output = kv_ur(a, b, c)
    return output
