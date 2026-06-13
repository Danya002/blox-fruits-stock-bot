import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxfruitscode.com/blox-fruits-stock-live-right-now/"
response = requests.get(url)

text = response.text

pos = text.find("Normal Stock")

if pos != -1:
    message = text[pos:pos+2500]
else:
    message = "Normal Stock не найден"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
