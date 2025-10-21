import strawberry
from typing import List

# ---- Data Types ----
@strawberry.type
class Weather:
    location: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    timestamp: str

@strawberry.type
class Stock:
    symbol: str
    name: str
    price: float
    change: float
    change_percent: float
    volume: int
    timestamp: str

@strawberry.type
class NewsArticle:
    title: str
    link: str
    summary: str
    published: str

@strawberry.type
class DatabaseRecord:
    id: int
    name: str
    category: str
    value: float
    created_at: str
