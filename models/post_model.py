from models.autor_model import AutorModel
from models.tag_model import TagModel
from core.configs import settings
from datetime import datetime
import sqlalchemy.orm as orm
from typing import List
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)


# Post pode ter várias tags
tags_post = Table(
    'tags_post',
    settings.DBBaseModel.metadata,
    Column('id_post', Integer, ForeignKey('post.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)

# Post pode ter vários comentários
comentarios_post = Table(
    'comentarios_post',
    settings.DBBaseModel.metadata,
    Column('id_post', Integer, ForeignKey('post.id')),
    Column('id_comentario', Integer, ForeignKey('comentarios.id'))
)


class PostModel(settings.DBBaseModel):
    '''Post do blog'''
    __tablename__: str = 'post'
    __allow_unmapped__ = True

    id: int = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    titulo: str = Column(String(200))
    data: datetime = Column(
        DateTime, 
        default=datetime.now,
        index=True
    )

    # Um posst pode ter várias tags
    tags: List[TagModel] = orm.relationship(
        'TagModel',
        secondary=tags_post,
        backref='tagp',
        lazy='joined'
    )

    imagem: str = Column(String(100)) # 900x400
    texto: str = Column(String(1000))

    # Um post pode ter vários comentários
    comentarios: List[object] = orm.relationship(
        'ComentarioModel',
        secondary=comentarios_post,
        backref='comentario'
    )
    id_autor: int = Column(
        Integer,
        ForeignKey('autores.id')
    )
    autor: AutorModel = orm.relationship(
        'AutorModel',
        lazy='joined'
    )
