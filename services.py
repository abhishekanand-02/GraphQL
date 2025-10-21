import requests
import feedparser
import sqlite3
import os
from datetime import datetime
from typing import List
from models import Weather, Stock, NewsArticle, DatabaseRecord


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str = "Hyderabad") -> Weather:
        if not self.api_key:
            raise RuntimeError("OPENWEATHER_API_KEY not found in environment variables. Please set a valid key.")
        
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return Weather(
            location=f"{data['name']}, {data['sys']['country']}",
            temperature=data['main']['temp'],
            description=data['weather'][0]['description'],
            humidity=data['main']['humidity'],
            wind_speed=data['wind']['speed'],
            timestamp=datetime.now().isoformat()
        )


class StockService:
    def __init__(self):
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        self.base_url = "https://www.alphavantage.co/query"
    
    def get_stock_data(self, symbol: str = "TCS.BSE") -> Stock:
        if not self.api_key:
            raise RuntimeError("ALPHA_VANTAGE_API_KEY not found in environment variables. Please set a valid key.")
        
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        quote = data.get("Global Quote", {})
        if not quote:
            raise RuntimeError(f"No stock data received for symbol {symbol}")
        
        price = float(quote.get("05. price", 0))
        change = float(quote.get("09. change", 0))
        change_percent = float(quote.get("10. change percent", "0%").replace("%", ""))
        volume = int(quote.get("06. volume", 0))
        
        return Stock(
            symbol=symbol,
            name=f"{symbol} Stock",
            price=price,
            change=change,
            change_percent=change_percent,
            volume=volume,
            timestamp=datetime.now().isoformat()
        )


class NewsService:
    def get_news(self, limit: int = 5) -> List[NewsArticle]:
        # Using BBC News RSS feed
        feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
        feed = feedparser.parse(feed_url)
        
        if not feed.entries:
            raise RuntimeError("Failed to fetch news feed from BBC")
        
        articles = []
        for entry in feed.entries[:limit]:
            articles.append(NewsArticle(
                title=entry.title,
                link=entry.link,
                summary=entry.get("summary", entry.title),
                published=entry.get("published", datetime.now().isoformat())
            ))
        
        return articles


class DatabaseService:
    def __init__(self):
        self.db_path = "sample_data.db"
        self.init_database()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                value REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute("SELECT COUNT(*) FROM products")
        if cursor.fetchone()[0] == 0:
            sample_data = [
                ("Laptop", "Electronics", 45000.00),
                ("Smartphone", "Electronics", 25000.00),
                ("Book", "Education", 500.00),
                ("T-Shirt", "Clothing", 800.00),
                ("Coffee Mug", "Kitchen", 200.00)
            ]
            cursor.executemany(
                "INSERT INTO products (name, category, value) VALUES (?, ?, ?)",
                sample_data
            )
        
        conn.commit()
        conn.close()
    
    def get_records(self, limit: int = 5) -> List[DatabaseRecord]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM products ORDER BY created_at DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        
        records = []
        for row in rows:
            records.append(DatabaseRecord(
                id=row[0],
                name=row[1],
                category=row[2],
                value=row[3],
                created_at=row[4]
            ))
        
        conn.close()
        return records
