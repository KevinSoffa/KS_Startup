from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi import FastAPI


app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory='templates')

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')


@app.get('/', name='index')
async def index(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('home/index.html', context=context)


@app.get('/about', name='about')
async def about(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('about/about.html', context=context)


@app.get('/contact', name='contact')
async def contact(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('contact/contact.html', context=context)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app='main:app', 
        host='0.0.0.0', 
        port=8000, 
        log_level='info'
    )
