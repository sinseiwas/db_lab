from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

# import asyncio
from contextlib import asynccontextmanager
import config


engine = create_async_engine(
    url=config.settings.DATABASE_URL_asyncpg,
    # echo=True,

)


session = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=True,
    class_=AsyncSession,

)


@asynccontextmanager
async def get_session():
    async with session() as db_session:  # Изменено имя переменной на db_session
        yield db_session
        await db_session.commit()


class Base(DeclarativeBase):
    pass

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)