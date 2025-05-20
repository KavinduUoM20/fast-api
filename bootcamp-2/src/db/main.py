from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import config
from src.books.models import BookModel

engine = AsyncEngine(
    create_engine(
    url=config.DATABASE_URL,
    echo=True
))

async def init_db()->None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        # statement = text("SELECT 'Hello';")
        # result = await conn.execute(statement)
        # print(result.all())

async def get_session()->AsyncSession:
    pass