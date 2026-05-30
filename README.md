# 🚀 Token Insight API

A FastAPI-based API that fetches real-time cryptocurrency market data from CoinGecko and generates sentiment insights based on 24-hour price movements.

## ✨ Features

- Real-time cryptocurrency data from CoinGecko
- Market metrics:
  - Current Price
  - Market Cap
  - Trading Volume
  - 24h Price Change
- Rule-based sentiment analysis
- FastAPI REST API
- Interactive Swagger documentation

## 🛠️ Tech Stack

- Python
- FastAPI
- Requests
- CoinGecko API

## ⚙️ Installation

```bash
git clone https://github.com/iamayush07032004/token-insight-api.git
cd token-insight-api

pip install -r requirements.txt
uvicorn main:app --reload
```

## 📖 API Endpoints

### Health Check

```http
GET /
```

### Get Token Insight

```http
POST /api/token/{id}/insight
```

Example:

```http
POST /api/token/bitcoin/insight
```

## 🪙 Test Coin IDs

| Coin | ID |
|--------|--------|
| Bitcoin | `bitcoin` |
| Ethereum | `ethereum` |
| Solana | `solana` |
| Dogecoin | `dogecoin` |
| Cardano | `cardano` |
| Ripple | `ripple` |


## 📚 API Docs

- Swagger UI: `http://127.0.0.1:8000/docs`

## 🧠 Sentiment Logic

| 24h Change | Sentiment |
|------------|------------|
| > 5% | Strongly Bullish |
| 0% – 5% | Bullish |
| -5% – 0% | Bearish |
| < -5% | Strongly Bearish |

## 👨‍💻 Author

**Ayush Yadav**

GitHub: https://github.com/iamayush07032004
