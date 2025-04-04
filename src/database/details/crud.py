from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database.details.models import Detail

async def add_detail(session: AsyncSession):
    new_detail = Detail(
        name="1",
        size="5x5",
        operation_amount=1,
        date="25.02.25"
    )

async def get_detail(session: AsyncSession, id):
    stmt = select(Detail).where(
        Detail.id == id,
    )
    result = await session.execute(stmt)
    detail = result.scalar_one_or_none()

    return detail


async def get_all_details(session: AsyncSession):
    stmt = select(Detail)
    result = await session.execute(stmt)
    details = result.all()

    if details is None:
            return {"error": "Details not found"}
    result = [
        {
            "id": detail.id,
            "name": detail.name,
            "size": detail.size,
            "operation_amount": detail.operation_amount,
            "start_date": detail.start_date,
            "end_date": detail.end_date
        }
        for detail, in details
    ]
    return result