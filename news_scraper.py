import requests
import json
from datetime import datetime

# --- CONFIGURATION ---
# We use the official Hacker News API (Firebase) - No Key Needed
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Keywords Rakesh Sir might be interested in
KEYWORDS = ["AI", "Python", "Data", "Startup", "India", "Tech", "Automate"]

print(f"--- 🤖 Pet OS Research Assistant ---")
print(f"Fetching top tech stories for: {datetime.now().strftime('%Y-%m-%d')}")
print("-" * 50)

def fetch_tech_news():
    try:
        # 1. Get the IDs of the top 50 stories
        response = requests.get(TOP_STORIES_URL)
        story_ids = response.json()[:30]  # Scan top 30 to save time
        
        found_stories = []

        print("Scanning headlines...", end="")
        
        for sid in story_ids:
            # 2. Get details for each story
            story_resp = requests.get(ITEM_URL.format(sid))
            story_data = story_resp.json()
            
            title = story_data.get('title', 'No Title')
            url = story_data.get('url', 'No URL')
            score = story_data.get('score', 0)
            
            # 3. Filter: Is this relevant? (Contains keyword OR has high score > 100)
            # We check if any keyword is in the title (Case insensitive)
            is_relevant = any(k.lower() in title.lower() for k in KEYWORDS)
            
            if is_relevant or score > 150:
                found_stories.append({
                    'title': title,
                    'url': url,
                    'score': score
                })
                print(".", end="", flush=True)

        print("\n" + "="*50)
        print(f"✅ FOUND {len(found_stories)} HIGH-SIGNAL STORIES")
        print("="*50)
        
        for i, story in enumerate(found_stories, 1):
            print(f"\n{i}. {story['title']}")
            print(f"   🔥 Score: {story['score']} | 🔗 {story['url']}")
            print(f"   Suggest for Newsletter? {'YES' if story['score'] > 200 else 'Maybe'}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_tech_news()
