from models.area_model import AreaModel
from core.configs import settings
import sqlalchemy.orm as orm
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)


class DuvidaModel(settings.DBBaseModel):
    __tablename__: str = 'duvida'
    __allow_unmapped__ = True

    id: int = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    id_area: int = Column(
        Integer, 
        ForeignKey('areas.id')
    )
    area: AreaModel = orm.relationship(
        'AreaModel', 
        lazy='joined'
    )
    titulo: str = Column(String(200))
    reposta: str = Column(String(400))
