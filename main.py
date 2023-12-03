from os import environ

from telethon import TelegramClient, events

API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")

client = TelegramClient('session', API_ID, API_HASH)

async def buy_event(stock, value):
    print(f"Buy event: Stock {stock}, value {value}")

async def sell_event(stock, value):
    print(f"Sell event: Stock {stock}, value {value}")

@client.on(events.NewMessage(chats="@BotFather"))
async def my_event_handler(event):
    if "buy" in event.text.lower():
        await buy_event("GOLD",  5)
    if "sell" in event.text.lower():
        await sell_event("GOLD", 5)

client.start()
client.run_until_disconnected()