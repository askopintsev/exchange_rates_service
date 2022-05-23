from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_service.app.database import get_session
from api_service.app.models import Record


api = APIRouter(
    prefix="/currency",
)


@api.get("/{char_code}")
async def get_exchange_rate(char_code: str, session: AsyncSession = Depends(get_session)):
    rate = await Record.get_last_rate(session, char_code)
    return {f"{char_code}": f"{rate}"}
