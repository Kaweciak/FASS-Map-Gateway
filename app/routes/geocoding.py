from fastapi import APIRouter

from app.schemas import GeocodeRequest
from app.services.geocoding_service import geocode

router = APIRouter()


@router.post("/geocode")
async def geocode_endpoint(request: GeocodeRequest):

    result = await geocode(request.query)

    return result