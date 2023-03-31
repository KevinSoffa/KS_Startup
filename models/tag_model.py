from sqlalchemy import Column, Integer, String
from core.configs import settings


class TagModel(settings.DBBaseModel):
    '''Várias tags em todo site'''
    __tablename__: str = 'tags'

    id: int = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    tag: str = Column(String(100))
