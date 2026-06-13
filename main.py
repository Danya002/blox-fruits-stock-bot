import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Получаем страницу со стоком
url = "https://bloxinformer.com/blox-fruits-stock/"
html = requests.get(url).text

# Отправляем первые 4000 символов страницы (для проверки)
message = html[:4000]

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
