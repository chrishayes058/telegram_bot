from os import environ
import requests

from telethon import TelegramClient, events

BASE_URL = "http://alpaca_trading_app"
BASE_PORT = 8000
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")

client = TelegramClient("session", API_ID, API_HASH)


async def buy_event(stock, quantity):
    url = f"{BASE_URL}:{BASE_PORT}/buy"
    data = {"name": stock, "quantity": quantity}

    result = requests.post(url, json=data)
    print(f"Sent BUY request with result: {result}")


async def sell_event(stock, quantity):
    print(f"Sell event: Stock {stock}, quantity {quantity}")


@client.on(events.NewMessage(chats="@BotFather"))
async def my_event_handler(event):
    if "buy" in event.text.lower():
        await buy_event("SPY", 5.0)
    if "sell" in event.text.lower():
        await sell_event("SPY", 5.0)


client.start()
client.run_until_disconnected()
