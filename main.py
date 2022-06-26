from fastapi import FastAPI, Request
from random import choices
from string import ascii_letters, digits
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


def create_url():
    url = choices(ascii_letters + digits, k=10)
    return "".join(url)


async def user_info_endpoint(request: Request):
    user_info: dict[str, str] = await request.json() # dict of preds known by the AI
    user_profile = request.headers  # dict of stuff like user's pfp, username etc
    return templates.TemplateResponse(
        "user_info.html.j2",
        {
            "request": request,
            "user_info": user_info,
            "user_profile": user_profile,
        },
    )


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates("templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/github")
async def github():
    return RedirectResponse("https://github.com/Hunter2809/HunAI")


@app.post("/create")
async def create_information_page(request: Request):
    url = create_url()
    app.add_api_route(url, user_info_endpoint(request))
