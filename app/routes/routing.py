from fastapi import APIRouter

from app.schemas import RouteRequest
from app.services.routing_service import calculate_route

router = APIRouter()


@router.post("/route")
async def route_endpoint(request: RouteRequest):

    result = await calculate_route(request)

    return {
        "length": result.get("length"),
        "duration": result.get("duration"),
        "geometry": result.get("geometry"),
        "parts": result.get("parts"),
        "routePoints": result.get("routePoints"),
    }