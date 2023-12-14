from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.get("/contact", response_class=HTMLResponse)
def read_contact(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("contact.html", context)