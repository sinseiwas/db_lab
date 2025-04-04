from database.database import init_db
import asyncio
from database.details.models import Detail
from database.workers.models import Worker
from database.operations.models import Operation


async def main():
    await init_db()


if __name__ == "__main__":
    asyncio.run(main())
