from sqlalchemy import Column, Integer, Date, Float
from sqlalchemy.ext.declarative import declarative_base

from app import session, engine

Base = declarative_base()
Base.query = session.query_property()


class Statistics(Base):

    __tablename__ = 'statistics'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    date = Column(Date, nullable=False)
    views = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    cost = Column(Float, nullable=True)
    cpc = Column(Float, nullable=True)
    cpm = Column(Float, nullable=True)

if not engine.dialect.has_table(engine, 'statistics'):
    Base.metadata.tables[f'{Statistics.__tablename__}'].create(engine)
