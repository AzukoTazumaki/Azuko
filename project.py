import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from models.models import InitDatabase
from db import SelectProjects
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# @app.on_event('startup')
# def startup():
#     init_db = InitDatabase()
#     init_db.create_db_and_tables()
#     init_db.create_projects()
#     init_db.close_session()


@app.get("/", response_class=RedirectResponse)
def index():
    return '/home'


@app.get("/home", response_class=HTMLResponse)
def index(request: Request):
    db_projects = SelectProjects()
    last_releases = db_projects.select_last_releases()
    products_list = db_projects.select_products()
    return templates.TemplateResponse(
        'home_content/home.html',
        {"request": request, "last_releases": last_releases,
         "products": [products_list[0], products_list[3]]}
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    db_projects = SelectProjects()
    products_list = db_projects.select_products()
    return templates.TemplateResponse(
        "products_content/all_products.html",
        {"request": request, "products": products_list})


@app.get("/products/{product_id}", response_class=HTMLResponse)
def albums_playlist(request: Request, product_id: int):
    db = SelectProjects()
    product = db.select_one_product(product_id)
    return templates.TemplateResponse(
        f"products_content/product.html", {"request": request, "product": product}
    )


@app.get("/projects", response_class=HTMLResponse)
def projects(request: Request):
    db_projects = SelectProjects()
    albums = db_projects.select_all_albums()
    singles = db_projects.select_singles()
    featurings = db_projects.select_featurings()
    return templates.TemplateResponse(
        "projects_content/projects.html", {
            "request": request,
            "albums": albums,
            "singles": singles,
            "featurings": featurings
        }
    )


@app.get("/playlist", response_class=HTMLResponse)
def playlist(request: Request):
    return templates.TemplateResponse("playlist_content/playlist.html", {'request': request})


@app.get("/playlist/albums/{album_id}", response_class=HTMLResponse)
def albums_playlist(request: Request, album_id: int):
    db_projects = SelectProjects()
    one_album = db_projects.select_one_album(album_id)
    return templates.TemplateResponse(
        "playlist_content/albums.html", {"request": request, "album": one_album}
    )


@app.get("/playlist/{project_name}", response_class=HTMLResponse)
def singles_playlist(request: Request, project_name: str):
    tracks = None
    playlist_title = project_name.capitalize()
    db_projects = SelectProjects()
    if project_name == 'singles':
        tracks = db_projects.select_singles()
    elif project_name == 'featurings':
        tracks = db_projects.select_featurings()
    return templates.TemplateResponse(
        "playlist_content/singles_featurings.html",
        {"request": request, "tracks": tracks, "title": playlist_title}
    )


@app.get("/order", response_class=HTMLResponse)
def order(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})


@app.exception_handler(StarletteHTTPException)
async def my_custom_exception_handler(request: Request, exception: StarletteHTTPException):
    if exception.status_code == 404:
        return templates.TemplateResponse('404.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('project:app', host='127.0.0.1', port=8000, reload=True)
