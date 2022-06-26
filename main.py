from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates("templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/github")
async def github():
    return RedirectResponse("https://github.com/Hunter2809")

@app.get("/hunai")
async def hunai():
    return RedirectResponse("https://github.com/Hunter2809/HunAi")
