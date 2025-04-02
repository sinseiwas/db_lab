from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.details.models import Detail


async def get_detail(session: AsyncSession, id):
    stmt = select(Detail).where(
        Detail.id == id,
    )
    result = await session.execute(stmt)
    detail = result.scalar_one_or_none()

    return detail