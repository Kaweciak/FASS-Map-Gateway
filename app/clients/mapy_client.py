import httpx

from app.config import settings


class MapyClient:

    async def geocode(self, query: str):

        async with httpx.AsyncClient(timeout=15.0) as client:

            response = await client.get(
                f"{settings.MAPY_BASE_URL}/geocode",
                params={
                    "query": query,
                    "apikey": settings.MAPY_API_KEY,
                }
            )

            response.raise_for_status()

            return response.json()

    async def route(
        self,
        start_lat: float,
        start_lon: float,
        end_lat: float,
        end_lon: float,
        route_type: str,
        geometry_format: str,
        avoid_toll: bool,
        avoid_highways: bool,
        waypoints: list,
        departure: str,
    ):

        params = {
            "start": f"{start_lon},{start_lat}",
            "end": f"{end_lon},{end_lat}",
            "routeType": route_type,
            "format": geometry_format,
            "avoidToll": str(avoid_toll).lower(),
            "avoidHighways": str(avoid_highways).lower(),
            "apikey": settings.MAPY_API_KEY,
        }

        if departure:
            params["departure"] = departure

        if waypoints:
            params["waypoints"] = "|".join(
                [
                    f"{point.lon},{point.lat}"
                    for point in waypoints
                ]
            )

        async with httpx.AsyncClient(timeout=30.0) as client:

            response = await client.get(
                f"{settings.MAPY_BASE_URL}/routing/route",
                params=params
            )

            response.raise_for_status()

            return response.json()