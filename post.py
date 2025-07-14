import os, requests, datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")
TIME      = datetime.datetime.utcnow() + datetime.timedelta(hours=3)

# Читаємо свіжий пост із Google-таблиці
url = "https://docs.google.com/spreadsheets/d/1eXPiP55es1oCycvh6RPNSboYXLw-vlFq27ZFfP8re0Q/gviz/tq?tqx=out:csv&gid=0&range=A2"
text = requests.get(url, timeout=10).text.strip()

if not text or text.lower() == "skip":
    exit(0)

# замінюємо {{DATE}} на поточну дату
text = text.replace("{{DATE}}", TIME.strftime("%d.%m %H:%M"))

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
)
