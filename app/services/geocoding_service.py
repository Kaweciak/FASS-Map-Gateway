from app.clients.mapy_client import MapyClient

client = MapyClient()


async def geocode(query: str):
    return await client.geocode(query)