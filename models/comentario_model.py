from models.post_model import PostModel
from core.configs import settings
from datetime import datetime
import sqlalchemy.orm as orm
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)


class ComentarioModel(settings.DBBaseModel):
    __tablename__: str = 'comentarios'
    __allow_unmapped__ = True

    id: int = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    data: datetime = Column(
        DateTime, 
        default=datetime.now, 
        index=True
    )
    id_post: int = Column(
        Integer,
        ForeignKey('post.id')
    )
    post: PostModel = orm.relationship(
        'PostModel',
        lazy='joined'
    )
    autor: str = Column(String(200))
    texto: str = Column(String(400))
