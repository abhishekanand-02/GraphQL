# 🚀 GraphQL Multi-Source Dashboard

> **Repository**: [https://github.com/abhishekanand-02/GraphQL](https://github.com/abhishekanand-02/GraphQL)

A comprehensive GraphQL application that demonstrates real-time data aggregation from multiple sources through a single GraphQL endpoint. This project showcases modern web development practices with FastAPI, GraphQL, and containerization.

## ✨ Key Features

This application integrates **4 different data sources** via GraphQL:

1. **🌤️ Weather Data** - Real-time weather information for Hyderabad using OpenWeather API
2. **📈 Stock Market Data** - Live BSE/NSE stock prices using Alpha Vantage API  
3. **🗄️ Database Records** - Sample product data from SQLite database
4. **📰 News Feed** - Latest headlines from BBC RSS feeds

## 📁 Project Structure

```
GraphQL_Application/
├── server.py          # FastAPI server with GraphQL endpoint
├── models.py          # GraphQL data models (Weather, Stock, News, Database)
├── services.py        # API service classes for external data sources
├── schema.py          # GraphQL schema definition and resolvers
├── index.html         # Responsive dashboard frontend
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker container configuration
├── docker-compose.yml # Multi-container orchestration
├── sample_data.db     # SQLite database with sample data
└── README.md         # Project documentation
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/abhishekanand-02/GraphQL.git
cd GraphQL/GraphQL_Application

# Build and run with Docker Compose
docker-compose up --build
```

**Access the application:**
- 🌐 **Dashboard**: http://localhost:8000 (Main UI with real-time data)
- 🔧 **GraphQL Playground**: http://localhost:8000/graphql (Interactive query interface)
- ❤️ **Health Check**: http://localhost:8000/health (Server status)

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/abhishekanand-02/GraphQL.git
cd GraphQL/GraphQL_Application

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

**Access the application:**
- 🌐 **Dashboard**: http://localhost:8000 (Main UI with real-time data)
- 🔧 **GraphQL Playground**: http://localhost:8000/graphql (Interactive query interface)
- ❤️ **Health Check**: http://localhost:8000/health (Server status)

## 🔑 API Configuration

The application requires API keys for external services. 

### Setup Environment Variables:

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your actual API keys:**
   ```bash
   # .env file
   OPENWEATHER_API_KEY=your_actual_openweather_api_key
   ALPHA_VANTAGE_API_KEY=your_actual_alpha_vantage_api_key
   ```

### Getting API Keys:

1. **OpenWeather API**: 
   - Visit: https://openweathermap.org/api
   - Sign up for a free account
   - Get your API key from the dashboard

2. **Alpha Vantage API**:
   - Visit: https://www.alphavantage.co/support/#api-key
   - Sign up for a free account
   - Get your API key from the dashboard

> **⚠️ Security Note**: Never commit real API keys to version control. Always use environment variables or secure key management systems.

## 🔍 GraphQL Queries

### Single Data Source Query
```graphql
query GetWeather {
  weather(city: "Hyderabad") {
    location
    temperature
    description
    humidity
    windSpeed
    timestamp
  }
}
```

### Multi-Source Data Query
```graphql
query GetAllData {
  weather(city: "Hyderabad") {
    location
    temperature
    description
    humidity
    windSpeed
    timestamp
  }
  stock(symbol: "RELIANCE.BSE") {
    symbol
    name
    price
    change
    changePercent
    volume
    timestamp
  }
  news(limit: 5) {
    title
    link
    summary
    published
  }
  databaseRecords(limit: 5) {
    id
    name
    category
    value
    createdAt
  }
}
```

### Available Query Parameters
- `weather(city: String)` - Get weather data for any city
- `stock(symbol: String)` - Get stock data for BSE/NSE symbols
- `news(limit: Int)` - Get latest news articles (default: 5)
- `databaseRecords(limit: Int)` - Get database records (default: 5)

## ✨ Application Features

- **🔄 Real-time Data**: Auto-refreshes every 30 seconds
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🛡️ Error Handling**: Graceful fallback to mock data if external APIs fail
- **🎨 Modern UI**: Beautiful gradient cards with smooth hover effects
- **🔧 GraphQL Playground**: Built-in query testing and exploration interface
- **🐳 Docker Support**: Easy deployment with containerization
- **⚡ Fast Performance**: Optimized queries and efficient data fetching

## 🛠️ Technology Stack

### Backend Technologies
- **FastAPI** - Modern, fast Python web framework for building APIs
- **Strawberry GraphQL** - Type-safe GraphQL library for Python
- **SQLite** - Lightweight, serverless database for local data storage
- **Requests** - HTTP library for making API calls to external services
- **Feedparser** - RSS feed parsing library for news aggregation

### Frontend Technologies
- **HTML5** - Semantic markup with modern web standards
- **CSS3** - Advanced styling with gradients, animations, and responsive design
- **Vanilla JavaScript** - Pure JavaScript for GraphQL client implementation

### DevOps & Deployment
- **Docker** - Containerization for consistent deployment environments
- **Docker Compose** - Multi-container orchestration and service management
- **Uvicorn** - ASGI server for running FastAPI applications

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Dashboard homepage with real-time data visualization |
| `POST` | `/graphql` | GraphQL endpoint for data queries and mutations |
| `GET` | `/health` | Health check endpoint for monitoring |

## 🔧 Development Guide

### Adding New Data Sources
1. Create a new service class in `services.py`
2. Define the data model in `models.py`
3. Add GraphQL resolver in `schema.py`
4. Update the frontend in `index.html`

### Customizing the Application
- **Backend**: Modify `server.py` for new routes and middleware
- **GraphQL Schema**: Update `schema.py` and `models.py` for new data types
- **Frontend**: Edit `index.html` for UI/UX improvements
- **Database**: Extend `services.py` for additional data operations

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **API Rate Limits** | Application automatically falls back to mock data |
| **CORS Issues** | CORS is configured to allow all origins for development |
| **Database Issues** | SQLite database is created automatically on first run |
| **Port Conflicts** | Change port in `docker-compose.yml` or server command |
| **Docker Issues** | Ensure Docker is running and ports 8000 is available |

## 📄 License

This project is created for educational and demonstration purposes. Feel free to use and modify as needed.

---

**Repository**: [https://github.com/abhishekanand-02/GraphQL](https://github.com/abhishekanand-02/GraphQL)

**Author**: Abhishek Anand
