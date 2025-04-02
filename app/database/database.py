from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

# import asyncio
from app import config

from app.database.details.models import metadata_obj as md_det
from app.database.workers.models import metadata_obj as md_work
from app.database.operations.models import metadata_obj as md_op


engine = create_async_engine(
    url=config.settings.DATABASE_URL_asyncpg,
    # echo=True,

)


session = async_sessionmaker(
    engine,

)


class Base(DeclarativeBase):
    pass

async def init_db():
    engine.echo = False
    md_det.create_all(engine)
    md_op.create_all(engine)
    md_work.create_all(engine)
    engine.echo = True