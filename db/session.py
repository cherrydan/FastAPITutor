###############################################
# BLOCK FOR COMMON INTERACTION WITH DATABASE  #
###############################################

# create async database engine
from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from settings import TEST_DATABASE_URL

engine = create_async_engine(TEST_DATABASE_URL, future=True, echo=True)

# create async session for the interaction with database
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
