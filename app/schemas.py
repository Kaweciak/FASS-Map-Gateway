from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Coordinate(BaseModel):
    lat: float
    lon: float


class RouteType(str, Enum):
    HIKING = "foot_hiking"
    CAR = "car_fast"


class RouteRequest(BaseModel):
    start: Coordinate
    end: Coordinate
    routeType: RouteType = RouteType.HIKING
    waypoints: Optional[List[Coordinate]] = []


class GeocodeRequest(BaseModel):
    query: str


class MarkerColor(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ORANGE = "orange"
    YELLOW = "yellow"
    BLACK = "black"
    WHITE = "white"


class MarkerSize(str, Enum):
    SMALL = "small"
    NORMAL = "normal"
    LARGE = "large"


class Marker(BaseModel):
    lon: float
    lat: float
    color: MarkerColor = MarkerColor.RED
    size: MarkerSize = MarkerSize.NORMAL
    label: Optional[str] = None


class StaticMapRequest(BaseModel):
    lon: float
    lat: float
    zoom: int = 13
    width: int = 600
    height: int = 400
    scale: int = 1
    padding: Optional[int] = None
    markers: Optional[List[Marker]] = []