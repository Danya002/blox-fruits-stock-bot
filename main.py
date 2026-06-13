import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxfruitscode.com/blox-fruits-stock-live-right-now/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

fruits = []

for fruit in soup.find_all("strong", class_="bfs-card-title"):
    fruits.append(fruit.text.strip())

# Удаляем повторы
fruits = list(dict.fromkeys(fruits))

message = response.text[response.text.find("Mirage Stock"):response.text.find("FAQ")]

for fruit in fruits:
    message += f"• {fruit}\n"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
