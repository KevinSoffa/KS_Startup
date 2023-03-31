from sqlalchemy import Column, Integer, String
from core.configs import settings


class AreaModel(settings.DBBaseModel):
    '''Dúvidas respondidas no FAQ'''
    __tablename__: str = 'areas'

    id: int = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    area: str = Column(String(100))
