from views.admin.membro_admin import membro_admin
from fastapi.routing import APIRouter
from datetime import datetime
from fastapi.requests import Request
from core.configs import settings


router = APIRouter(prefix='/admin')
router.include_router(membro_admin.router, prefix='/admin')


@router.get('/', name='admin_index')
async def admin_index(request: Request):
    context = {
        'request': request,
        'ano': datetime.now().year
    }

    return settings.TEMPLATES.TemplateResponse('admin/index.html', context=context)