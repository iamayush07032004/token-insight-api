from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API Running"}


@app.post("/api/token/{id}/insight")
def token_insight(id: str):



    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Invalid coin ID")

    data = response.json()

    token_data = {
        "id": data["id"],
        "symbol": data["symbol"],
        "name": data["name"],
        "market_data": {
            "current_price_usd": data["market_data"]["current_price"]["usd"],
            "market_cap_usd": data["market_data"]["market_cap"]["usd"],
            "total_volume_usd": data["market_data"]["total_volume"]["usd"],
            "price_change_percentage_24h": data["market_data"]["price_change_percentage_24h"]
        }
    }


    change = token_data["market_data"]["price_change_percentage_24h"]

    if change > 5:
        sentiment = "strongly bullish"
        reasoning = "Strong upward momentum in last 24h."

    elif change > 0:
        sentiment = "bullish"
        reasoning = "Price increased in last 24h."

    elif change < -5:
        sentiment = "strongly bearish"
        reasoning = "Strong downward movement in last 24h."

    else:
        sentiment = "bearish"
        reasoning = "Slight price drop or weak movement."

    insight = {
        "sentiment": sentiment,
        "reasoning": reasoning
    }


    return {
        "source": "coingecko",
        "token": token_data,
        "insight": insight,
        "model": {
            "provider": "mock-ai",
            "model": "rule-based-v1"
        }
    }