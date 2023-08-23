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
    last_releases = [
        ['../../static/images/last_releases/0.jpg', 'Supposed To Be', 'Azuko'],
        ['../../static/images/last_releases/1.jpg', 'with love from Azuko', 'Azuko'],
        ['../../static/images/last_releases/2.jpg', 'Лавина', 'Azuko, 88Ringo']
    ]
    products = [
        ['../../static/images/products/beats.jpg', '3000'],
        ['../../static/images/products/mixing_and_mastering.jpg', '2000', '1500']
    ]
    return templates.TemplateResponse('home_content/home.html',
                                      {"request": request,
                                       "last_releases": last_releases,
                                       "products": products
                                       })


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
