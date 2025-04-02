from database.database import init_db
import asyncio


async def main():
    await init_db()


if __name__ == "__main__":
    asyncio.run(main())
