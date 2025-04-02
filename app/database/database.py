from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

# import asyncio
import config


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
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)