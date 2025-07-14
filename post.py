import os, requests, datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")
TIME      = datetime.datetime.utcnow() + datetime.timedelta(hours=3)

MSG = f"""
🎉 Привіт з GitHub Actions!
📅 {TIME:%d.%m %H:%M} — тестовий пост від Рейвена
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": MSG.strip(), "parse_mode": "HTML"}
)
