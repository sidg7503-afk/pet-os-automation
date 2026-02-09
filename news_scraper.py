import requests
import json
from datetime import datetime

# --- CONFIGURATION ---
# Note: For a real deployment, use Environment Variables for keys.
# Get your keys from the links in README.md

TELEGRAM_BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"  # from @BotFather
TELEGRAM_CHAT_ID = "PASTE_YOUR_CHAT_ID_HERE"      # from @userinfobot
OPENAI_API_KEY = "PASTE_YOUR_OPENAI_KEY_HERE"     # from platform.openai.com

# Hacker News API (No Key Needed)
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Keywords for "Pet OS" Audience
KEYWORDS = ["AI", "Python", "Data", "Startup", "India", "Tech", "Bihar"]

print(f"--- 🤖 Pet OS Research Assistant v2.0 ---")
print(f"Fetching top tech stories for: {datetime.now().strftime('%Y-%m-%d')}")

def send_telegram_alert(message):
    """Sends the summary directly to your phone via Telegram"""
    if TELEGRAM_BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("   ⚠️ Telegram Token missing. Skipping alert.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
        print("   📲 Sent to Telegram!")
    except Exception as e:
        print(f"   ❌ Telegram Error: {e}")

def fetch_tech_news():
    try:
        response = requests.get(TOP_STORIES_URL)
        story_ids = response.json()[:30]  # Scan top 30 stories
        
        print("Scanning headlines...", end="")
        
        for sid in story_ids:
            story_resp = requests.get(ITEM_URL.format(sid))
            story_data = story_resp.json()
            
            title = story_data.get('title', 'No Title')
            url = story_data.get('url', 'No URL')
            score = story_data.get('score', 0)
            
            # Check for Keywords
            is_relevant = any(k.lower() in title.lower() for k in KEYWORDS)
            
            if is_relevant or score > 200:
                print(f"\n\n🔥 MATCH: {title}")
                print(f"   🔗 {url}")
                
                # Prepare Message
                msg = f"🚀 **Pet OS Alert**\n\n**{title}**\nScore: {score}\n[Read Article]({url})"
                
                # Send Alert
                send_telegram_alert(msg)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_tech_news()
