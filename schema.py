import strawberry
from typing import List
from models import Weather, Stock, NewsArticle, DatabaseRecord
from services import WeatherService, StockService, NewsService, DatabaseService

# ---- GraphQL Queries ----
@strawberry.type
class Query:
    @strawberry.field
    def weather(self, city: str = "Hyderabad") -> Weather:
        weather_service = WeatherService()
        return weather_service.get_weather(city)
    
    @strawberry.field
    def stock(self, symbol: str = "RELIANCE.BSE") -> Stock:
        stock_service = StockService()
        return stock_service.get_stock_data(symbol)
    
    @strawberry.field
    def news(self, limit: int = 5) -> List[NewsArticle]:
        news_service = NewsService()
        return news_service.get_news(limit)
    
    @strawberry.field
    def database_records(self, limit: int = 5) -> List[DatabaseRecord]:
        db_service = DatabaseService()
        return db_service.get_records(limit)
