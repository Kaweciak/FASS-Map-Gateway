from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Coordinate(BaseModel):
    lat: float
    lon: float


class RouteType(str, Enum):

    FOOT_FAST = "foot-fast"

    FOOT_HIKING = "foot-hiking"

    CAR_FAST = "car-fast"

    CAR_SHORT = "car-short"

    BICYCLE_ROAD = "bicycle-road"

    BICYCLE_MOUNTAIN = "bicycle-mountain"


class GeometryFormat(str, Enum):
    GEOJSON = "geojson"
    POLYLINE = "polyline"


class RouteRequest(BaseModel):

    start: Coordinate
    end: Coordinate

    routeType: RouteType = RouteType.FOOT_FAST

    format: GeometryFormat = GeometryFormat.GEOJSON

    avoidToll: bool = False

    avoidHighways: bool = False

    waypoints: Optional[List[Coordinate]] = []

    departure: Optional[str] = None


class GeocodeRequest(BaseModel):
    query: str


class StaticMapRequest(BaseModel):
    lat: float
    lon: float
    zoom: int = 15
    width: int = 600
    height: int = 400
    scale: int = 1
    padding: Optional[int] = None
    lang: Optional[str] = None
    # Each entry is a raw marker string, e.g. "color:red;size:normal;14.421,50.088"
    markers: List[str] = []
    # Each entry is a raw shape string, e.g. "color:green;path:[...]"
    shapes: List[str] = []