import os, requests, datetime, textwrap

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")
TIME_KYIV = datetime.datetime.utcnow() + datetime.timedelta(hours=3)

# --- Тут будуть готові тексти від Рейвена ---
TEXT = f"""
🎮 <b>Мікро-добірка від Рейвена</b>  
📅 {TIME_KYIV.strftime('%d.%m')} понеділок/четвер

🔹 <b>Безкоштовна гра тижня</b>: <a href="https://store.epicgames.com/ru/p/...">(посилання)</a>  
🔹 <b>Корисний твік</b>: у Windows 11 увімкніть «Hardware-accelerated GPU scheduling» → +2-5 % FPS  
🔹 <b>Анекдот</b>:
— Докторе, у мене залежність від Steam…
— Скільки ігор не зіграно?
— Триста сімдесят чотири.
— То це не залежність, а інвестиційний портфель! 😎
 
До зустрічі за 3 дні!
"""

payload = {
    "chat_id": CHAT_ID,
    "text": textwrap.dedent(TEXT).strip(),
    "parse_mode": "HTML",
    "disable_web_page_preview": True
}

r = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json=payload)
print(r.status_code, r.json())
trigger actions
