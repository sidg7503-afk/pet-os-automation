# 🤖 Pet OS Research Assistant

**Author:** Sachin Kumar (QuantLogic India)  
**Status:** v2.0 (Alpha)  
**Stack:** Python, HackerNews API, Telegram Bot

---

### 🎯 Problem
Curating tech news for the **Pet OS Newsletter** is manual and time-consuming. You need a way to filter the "Signal" from the "Noise" automatically.

### 💡 The Solution
I built this Python bot to act as a **24/7 Research Intern**.
1.  **Scans** global tech news (HackerNews).
2.  **Filters** for high-impact keywords (AI, Startups, India).
3.  **Alerts** you instantly on Telegram with the top stories.

---

### ⚙️ Setup & Configuration (How to get Keys)

To run this on your local machine, you need to fill in the `Configuration` section in the Python file.

#### 1. Get a Telegram Bot Token (Free)
1.  Open Telegram and search for **@BotFather**.
2.  Send the command `/newbot`.
3.  Name it `PetOS_Helper`.
4.  Copy the **HTTP API Token** it gives you.

#### 2. Get your Chat ID (Free)
1.  Open Telegram and search for **@userinfobot**.
2.  Click **Start**.
3.  Copy the `Id` number it replies with.

#### 3. Run the Script
```bash
pip install requests
python news_scraper.py
