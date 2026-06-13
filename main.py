import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxfruitsvalues.com/stock"
response = requests.get(url)

text = response.text

# Ищем первое вхождение слова "Kitsune"
pos = text.find("Kitsune")

if pos != -1:
    message = text[pos-500:pos+2000]
else:
    message = "Kitsune не найден"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
