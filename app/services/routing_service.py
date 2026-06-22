from app.clients.mapy_client import MapyClient

client = MapyClient()


async def calculate_route(request):

    return await client.route(
        start_lat=request.start.lat,
        start_lon=request.start.lon,
        end_lat=request.end.lat,
        end_lon=request.end.lon,
        route_type=request.routeType.value,
        waypoints=request.waypoints,
    )