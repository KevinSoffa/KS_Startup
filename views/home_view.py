from fastapi.routing import APIRouter
from fastapi.requests import Request
from core.configs import settings


router = APIRouter()

@router.get('/', name='index')
async def index(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('home/index.html', context=context)


@router.get('/about', name='about')
async def about(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('about/about.html', context=context)


@router.get('/contact', name='contact')
async def contact(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('contact/contact.html', context=context)


@router.get('/pricing', name='pricing')
async def pricing(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('pricing/pricing.html', context=context)


@router.get('/faq', name='faq')
async def faq(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('faq/faq.html', context=context)


@router.get('/blog-home', name='blog_home')
async def blog_home(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('blog/blog_home/blog_home.html', context=context)


@router.get('/blog-post', name='blog_post')
async def blog_post(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('blog/blog_post/blog_post.html', context=context)


@router.get('/portfolio-overview', name='portfolio_overview')
async def portfolio_overview(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('portfolio/portfolio_overview/portfolio_overview.html', context=context)


@router.get('/portfolio-item', name='portfolio_item')
async def portfolio_item(request: Request):
    context = {
        'request': request
    }
    return settings.TEMPLATES.TemplateResponse('portfolio/portfolio_item/portfolio_item.html', context=context)
