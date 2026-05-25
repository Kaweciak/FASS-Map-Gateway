from fastapi import FastAPI

from app.routes.geocoding import router as geocode_router
from app.routes.routing import router as routing_router

app = FastAPI(
    title="Map Gateway Service"
)

app.include_router(
    geocode_router,
    prefix="/api/maps"
)

app.include_router(
    routing_router,
    prefix="/api/maps"
)


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }