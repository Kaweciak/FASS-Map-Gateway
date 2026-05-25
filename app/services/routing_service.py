from app.clients.mapy_client import MapyClient

client = MapyClient()


async def calculate_route(request):

    return await client.route(
        start_lat=request.start.lat,
        start_lon=request.start.lon,
        end_lat=request.end.lat,
        end_lon=request.end.lon,
        route_type=request.routeType.value,
        geometry_format=request.format.value,
        avoid_toll=request.avoidToll,
        avoid_highways=request.avoidHighways,
        waypoints=request.waypoints,
        departure=request.departure,
    )