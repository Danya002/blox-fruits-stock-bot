```python
import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Получаем страницу со стоком
url = "https://bloxinformer.com/blox-fruits-stock/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Ищем названия фруктов
fruits = []

for img in soup.find_all("img"):
    alt = img.get("alt")
    if alt and "fruit" in alt.lower():
        fruits.append(alt)

# Удаляем повторы
fruits = list(dict.fromkeys(fruits))

# Формируем сообщение
if fruits:
    text = "🍎 Текущий сток Blox Fruits:\n\n"
    text += "\n".join(f"• {fruit}" for fruit in fruits)
else:
    text = "Не удалось получить сток."

# Отправляем сообщение
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": text
    }
)
```
