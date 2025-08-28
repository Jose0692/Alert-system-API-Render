import asyncio
from db.database import engine

async def test_connection():
    async with engine.begin() as conn:
        await conn.run_sync(lambda _: print("Conexión exitosa con PostgreSQL"))

if __name__ == "__main__":
    asyncio.run(test_connection())