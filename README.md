# Token Insight API

A FastAPI backend service that fetches cryptocurrency market data from CoinGecko and generates sentiment insights based on 24-hour price movements.

## Features

- Fetch real-time cryptocurrency data from CoinGecko
- Get current price, market cap, and trading volume
- Generate sentiment insights based on price movement
- Input validation for token IDs
- Error handling for invalid tokens
- Interactive API documentation with Swagger

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "API Running"
}
```

### Get Token Insight

```http
POST /api/token/{id}/insight
```

### Example Request

```http
POST /api/token/bitcoin/insight
```

### Example Response

```json
{
  "source": "coingecko",
  "token": {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin",
    "market_data": {
      "current_price_usd": 68000,
      "market_cap_usd": 1300000000000,
      "total_volume_usd": 25000000000,
      "price_change_percentage_24h": 6.2
    }
  },
  "insight": {
    "sentiment": "strongly bullish",
    "reasoning": "Strong upward momentum in last 24h."
  },
  "model": {
    "provider": "mock-ai",
    "model": "rule-based-v1"
  }
}
```

## Test Data

### Coin IDs

| Coin | ID |
|------|------|
| Bitcoin | bitcoin |
| Ethereum | ethereum |
| Solana | solana |
| Dogecoin | dogecoin |
| Cardano | cardano |
| Ripple | ripple |

### Example Requests

```http
POST /api/token/bitcoin/insight
POST /api/token/ethereum/insight
POST /api/token/solana/insight
```

## Sentiment Logic

| 24h Price Change | Sentiment |
|------------------|------------|
| > 5% | Strongly Bullish |
| 0% to 5% | Bullish |
| -5% to 0% | Bearish |
| < -5% | Strongly Bearish |

## Tech Stack

- Python
- FastAPI
- Requests
- Python-dotenv
- CoinGecko API
## Run with Docker

### Build Docker Image

```bash
docker build -t token-insight-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 token-insight-api
```

### Access Application

```text
http://localhost:8000
```

### Swagger Documentation

```text
http://localhost:8000/docs
```

## Repository

GitHub Repository:

https://github.com/iamayush07032004/token-insight-api
