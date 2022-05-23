from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api_service.app.config import Config


engine = create_async_engine(Config.DB_CONFIG, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
