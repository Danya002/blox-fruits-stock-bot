import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxinformer.com/blox-fruits-stock/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

fruits = []

for img in soup.find_all("img"):
  alt = img.get("alt")
  if alt and "fruit" in alt.lower():
    fruits.append(alt)

fruits = list(dict.fromkeys(fruits))

if fruits:
  text = "🍎 Текущий сток Blox Fruits:\n\n"
  text += "\n".join(f"• {fruit}" for fruit in fruits)
else:
  text = "Не удалось получить сток."

requests.post(
  f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
  data={
    "chat_id": CHAT_ID,
    "text": text
  }
)
