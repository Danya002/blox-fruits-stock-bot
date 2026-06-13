import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxinformer.com/blox-fruits-stock/"
response = requests.get(url)

text = response.text

# Ищем слово Fruit
pos = text.find("Fruit")

if pos != -1:
    message = text[pos:pos+3000]
else:
    message = "Слово Fruit не найдено"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
