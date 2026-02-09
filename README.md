# 🤖 Pet OS Research Assistant

**Author:** Sachin Kumar (QuantLogic India)  
**Status:** v1.0 (Live)  
**Tech Stack:** Python, Requests, Hacker News API

---

### 🎯 Problem Statement
Curating high-quality tech news for a newsletter (like *Pet OS*) is time-consuming. Sifting through noise to find "Signal" requires manual effort.

### 💡 The Solution
I built this Python automation script to act as a **24/7 Research Intern**. 
It connects to the Hacker News API to fetch real-time global tech trends and filters them based on relevance to the Indian Tech Ecosystem.

### ⚙️ How It Works
1.  **Fetch:** Polls the top 50 stories from the Hacker News public API.
2.  **Filter:** Scans headlines for high-impact keywords (`AI`, `Python`, `Startup`, `India`).
3.  **Rank:** Prioritizes stories with a "Virality Score" > 150 points.
4.  **Report:** Generates a clean list of links ready for the newsletter.

### 🚀 Usage
```bash
python news_scraper.py
