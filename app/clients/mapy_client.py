from typing import Optional, Union

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

    async def static_map(
        self,
        lon: float,
        lat: float,
        zoom: int,
        width: int,
        height: int,
        scale: int,
        padding: Optional[int],
        markers: list,
    ) -> bytes:

        # httpx accepts repeated keys as a list of (key, value) tuples
        params: list[tuple[str, Union[str, int, float]]] = [
            ("lon", lon),
            ("lat", lat),
            ("zoom", zoom),
            ("width", width),
            ("height", height),
            ("scale", scale),
            ("format", "png"),
            ("mapset", "outdoor"),
            ("lang", "pl"),
            ("apikey", settings.MAPY_API_KEY),
        ]

        if padding is not None:
            params.append(("padding", padding))

        # Each marker becomes a separate "markers" query param.
        # Format: color:<c>;size:<s>[;label:<l>];<lon>,<lat>
        for marker in markers:
            parts = [
                f"color:{marker.color.value}",
                f"size:{marker.size.value}",
            ]
            if marker.label:
                parts.append(f"label:{marker.label}")
            parts.append(f"{marker.lon},{marker.lat}")
            params.append(("markers", ";".join(parts)))

        async with httpx.AsyncClient(timeout=30.0) as client:

            response = await client.get(
                f"{settings.MAPY_BASE_URL}/static/map",
                params=params,
            )

            response.raise_for_status()

            return response.content