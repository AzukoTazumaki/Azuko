import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from models.Albums import Albums
from names import ProjectNames
from models.models import InitDatabase
from db_projects import SelectProjects

app = FastAPI()
init_db = InitDatabase()
db_projects = SelectProjects()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event('startup')
def startup():
    init_db.create_db_and_tables()
    init_db.create_projects()
    init_db.close_session()


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
    featurings = ProjectNames('featurings')
    return templates.TemplateResponse("projects_content/projects.html", {
        "request": request,
        "albums": db_projects.select_all_albums(),
        "singles": db_projects.select_singles(),
        "featurings": featurings.get_single_or_featuring_info()
    })


@app.get("/playlist", response_class=HTMLResponse)
async def playlist(request: Request):
    return templates.TemplateResponse("playlist_content/playlist.html", {'request': request})


@app.get("/playlist/albums/{album_id}", response_class=HTMLResponse)
async def albums_playlist(request: Request, album_id: int):
    return templates.TemplateResponse("playlist_content/albums.html", {"request": request, "album": db_projects.select_one_album(album_id)})


@app.get("/playlist/singles", response_class=HTMLResponse)
async def singles_playlist(request: Request):
    return templates.TemplateResponse("playlist_content/singles.html", {"request": request, "singles": db_projects.select_singles()})


@app.get("/test", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})


# @app.get("/playlist/albums/{albums_id}")
# async def albums_playlist(albums_id: int, albums: Albums):
#     return {'albums_id': albums_id, **albums.dict()}


if __name__ == '__main__':
    uvicorn.run('project:app', host='127.0.0.1', port=8000, reload=True)
