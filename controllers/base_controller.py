from core.database import get_session
from fastapi.requests import Request
from sqlalchemy.future import select
from typing import Optional, List


class BaseController:
    """Definando construtor"""
    def __init__(self, request: Request, model: object) -> None:
        self.request: Request = request
        self.model: object = model


    async def get_all_crud(self) -> Optional[List[object]]:
        """
        Retorna todos os registros do Model
        """
        async with get_session() as session:
            query = select(self.model)
            result = await session.execute(query)

            return result.scalars().all()
        

    async def get_one_crud(self, id_obj: int) -> Optional[object]:
        """
        Retorna o obj especificado pelo ID ou None
        """
        async with get_session() as session:
            obj: self.model = await session.get(self.model, id_obj)

            return obj
        
        
    async def post_crud(self) -> None:
        raise NotImplementedError('Você precisa implementar este método')
    

    async def put_crud(self, obj: object) -> None:
        raise NotImplementedError('Você precisa implementar este método')


    async def del_crud(self, id_obj: int) -> None:
        async with get_session() as session:
            obj: self.model = await session.get(self.model, id_obj)

            if obj:
                await session.delete(obj)
                await session.commit()
