from fastapi import APIRouter

from database.details.crud import get_all_details
from database.database import get_session

router = APIRouter()


@router.get("/detail", tags=["Details"])
async def get_detail_():
    async with get_session() as session:
        details = await get_all_details(session)
        return details
