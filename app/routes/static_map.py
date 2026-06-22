from fastapi import APIRouter
from fastapi.responses import Response

from app.schemas import StaticMapRequest
from app.services.static_map_service import get_static_map

router = APIRouter()


@router.post("/static-map", response_class=Response)
async def static_map_endpoint(request: StaticMapRequest):

    image_bytes = await get_static_map(request)

    return Response(content=image_bytes, media_type="image/png")