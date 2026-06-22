from app.clients.mapy_client import MapyClient

client = MapyClient()


async def get_static_map(request) -> bytes:
    return await client.static_map(
        lon=request.lon,
        lat=request.lat,
        zoom=request.zoom,
        width=request.width,
        height=request.height,
        scale=request.scale,
        padding=request.padding,
        markers=request.markers or [],
    )