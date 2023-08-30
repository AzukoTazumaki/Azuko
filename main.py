import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    last_releases_list = [
        ['../../static/images/last_releases/0.jpg', 'Supposed To Be', 'Azuko'],
        ['../../static/images/last_releases/1.jpg', 'with love from Azuko', 'Azuko'],
        ['../../static/images/last_releases/2.jpg', 'Лавина', 'Azuko, 88Ringo']
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


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
