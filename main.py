from os import environ
import requests

from telethon import TelegramClient, events

BASE_URL = "http://alpaca_trading_app"
BASE_PORT = 8000
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")

client = TelegramClient("session", API_ID, API_HASH)


async def buy_event(stock, value):
    url = f"{BASE_URL}:{BASE_PORT}/buy"
    data = {"name": "SPY", "quantity": 1.0}

    result = requests.post(url, json=data)
    print(f"Sent BUY request with result: {result}")


async def sell_event(stock, value):
    print(f"Sell event: Stock {stock}, value {value}")


@client.on(events.NewMessage(chats="@BotFather"))
async def my_event_handler(event):
    if "buy" in event.text.lower():
        await buy_event("GOLD", 5)
    if "sell" in event.text.lower():
        await sell_event("GOLD", 5)


client.start()
client.run_until_disconnected()
