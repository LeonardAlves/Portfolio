from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import PROJECTS, get_project

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    tags = sorted({t for p in PROJECTS for t in p["tags"]})
    return templates.TemplateResponse(
        request, "home.html", {"projects": PROJECTS, "tags": tags}
    )


@app.get("/projects", response_class=HTMLResponse)
def project_list(request: Request, tag: str | None = None):
    items = [p for p in PROJECTS if not tag or tag in p["tags"]]
    return templates.TemplateResponse(
        request, "partials/project_list.html", {"projects": items}
    )


@app.get("/projects/{slug}", response_class=HTMLResponse)
def project_detail(request: Request, slug: str):
    project = get_project(slug)
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return templates.TemplateResponse(
        request, "project_detail.html", {"project": project}
    )