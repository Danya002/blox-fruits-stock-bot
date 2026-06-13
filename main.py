import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://bloxfruitscode.com/blox-fruits-stock-live-right-now/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Таймер
timer = "--:--:--"
timer_tag = soup.find("span", class_="bfs-stock-timer-value")
if timer_tag:
    timer = timer_tag.text.strip()

# Получаем все карточки фруктов
cards = soup.find_all("li", class_="bfs-stock-card")

normal = []
mirage = []

current = normal

for card in cards:
    title = card.find("strong", class_="bfs-card-title")
    prices = card.find_all("span", class_="bfs-price-value")

    if title and len(prices) >= 2:
        fruit = title.text.strip()
        beli = prices[0].text.strip()
        robux = prices[1].text.strip()

        current.append(
            f"🍏 {fruit}\n💵 {beli} Beli | {robux} Robux"
        )

# Делим список пополам
half = len(normal) // 2
mirage = normal[half:]
normal = normal[:half]

message = f"""🍎 NORMAL STOCK

⏳ Следующий сток через: {timer}

"""

message += "\n\n".join(normal)

message += "\n\n🌙 MIRAGE STOCK\n\n"

message += "\n\n".join(mirage)

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
