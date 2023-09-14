from typing import Union

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from names import ProjectNames

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=RedirectResponse)
async def index():
    return '/home'


@app.get("/home", response_class=HTMLResponse)
async def index(request: Request):
    last_releases_list = [
        ['0.jpg', 'FADED.', 'Azuko'],
        ['1.jpg', 'Supposed To Be', 'Azuko'],
        ['2.jpg', 'with love from Azuko', 'Azuko']
    ]
    products_list = [
        ['beats.jpg', '3000'],
        ['mixing_and_mastering.jpg', '5000', '3750']
    ]
    return templates.TemplateResponse('home_content/home.html',
                                      {"request": request,
                                       "last_releases": last_releases_list,
                                       "products": products_list})


@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    products_list = [
        ["beats.jpg", 'Beats', '3000'],
        ['mixing.jpg', 'Mixing', '3500'],
        ['mastering.jpg', 'Mastering', '1500'],
        ['mixing_and_mastering.jpg', 'Mixing & Mastering', '5000', '3750']
    ]
    return templates.TemplateResponse("products_content/products.html",
                                      {"request": request,
                                       "products": products_list})


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    albums = ProjectNames('carousel_albums')
    singles = ProjectNames('carousel_singles')
    featurings = ProjectNames('carousel_featurings')
    return templates.TemplateResponse("projects_content/projects.html",
                                      {
                                          "request": request,
                                          "albums": albums.get_project_info(),
                                          "singles": singles.get_project_info(),
                                          "featurings": featurings.get_project_info()
                                      })


@app.get("/playlist", response_class=HTMLResponse)
async def playlist(request: Request):
    return templates.TemplateResponse("playlist_content/playlist.html", {'request': request})


@app.get("/albums", response_class=HTMLResponse)
async def albums_playlist(request: Request):
    return templates.TemplateResponse("albums_content/albums.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run('project:app', host='127.0.0.1', port=8000, reload=True)
