import os, requests, datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")
TIME      = datetime.datetime.utcnow() + datetime.timedelta(hours=3)

# ↓↓↓ ось саме посилання на gist
url = f"https://gist.githubusercontent.com/Dimon3063/f53bcb68373890e891cd141d1475008b/raw/post.txt?t={int(datetime.datetime.utcnow().timestamp())}"

text = requests.get(url, timeout=10).text.strip()
if not text or text.lower() == "skip":
    exit(0)

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
)
