"""
Web Scraper (Basic)
Difficulty: Medium
Concepts: requests, BeautifulSoup, HTML Parsing
"""

import csv
import re
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install required packages:")
    print("  pip install requests beautifulsoup4")
    exit(1)


def fetch_page(url):
    """Fetch and parse a webpage."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None


def scrape_hacker_news(limit=10):
    """Scrape top stories from Hacker News."""
    url = "https://news.ycombinator.com/"
    soup = fetch_page(url)
    if not soup:
        return []

    stories = []
    items = soup.find_all("tr", class_="athing")

    for item in items[:limit]:
        try:
            title_tag = item.find("span", class_="titleline").find("a")
            title = title_tag.get_text(strip=True)
            link = title_tag["href"]
            if link.startswith("item?"):
                link = urljoin(url, link)

            # Get score from the next row
            next_row = item.find_next_sibling("tr")
            score_text = "0"
            if next_row:
                score_tag = next_row.find("span", class_="score")
                if score_tag:
                    score_text = score_tag.get_text(strip=True)

            score = re.search(r"(\d+)", score_text)
            score = int(score.group(1)) if score else 0

            stories.append({
                "title": title,
                "link": link,
                "score": score
            })
        except (AttributeError, KeyError):
            continue

    return stories


def scrape_generic(url, title_selector="h2", link_selector="a"):
    """Generic scraper for simple blogs/news sites."""
    soup = fetch_page(url)
    if not soup:
        return []

    stories = []
    titles = soup.find_all(title_selector, limit=10)

    for title_tag in titles:
        try:
            title = title_tag.get_text(strip=True)
            link_tag = title_tag.find(link_selector) or title_tag
            link = link_tag.get("href", "")
            if link and not link.startswith("http"):
                link = urljoin(url, link)

            stories.append({
                "title": title,
                "link": link,
                "score": 0
            })
        except Exception:
            continue

    return stories


def display_stories(stories, keyword=None):
    """Display stories in a formatted table."""
    if keyword:
        stories = [s for s in stories if keyword.lower() in s["title"].lower()]
        print(f"\n🔍 Filtered by keyword: '{keyword}'")

    if not stories:
        print("📭 No stories found.")
        return

    print(f"\n{'─' * 80}")
    print(f"  {'#':<4}{'Score':<8}{'Title'}")
    print(f"{'─' * 80}")

    for i, s in enumerate(stories, 1):
        title = s["title"][:55] + "..." if len(s["title"]) > 55 else s["title"]
        score_str = f"{s['score']} pts" if s["score"] > 0 else "N/A"
        print(f"  {i:<4}{score_str:<8}{title}")

    print(f"{'─' * 80}")
    print(f"  Total: {len(stories)} stories")


def save_to_csv(stories, filename="headlines.csv"):
    """Save stories to CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link", "score"])
        writer.writeheader()
        for s in stories:
            writer.writerow(s)
    print(f"\n📤 Saved to {filename}")


def main():
    """Main application loop."""
    print("=" * 60)
    print("🌐 WEB SCRAPER")
    print("=" * 60)

    stories = []

    while True:
        print("\n📂 Menu:")
        print("  1. 🔥 Scrape Hacker News")
        print("  2. 🌐 Scrape custom URL")
        print("  3. 📋 View results")
        print("  4. 🔍 Filter by keyword")
        print("  5. 💾 Save to CSV")
        print("  6. 🚪 Exit")

        choice = input("\nChoose (1-6): ").strip()

        if choice == "1":
            print("\n⏳ Fetching Hacker News...")
            stories = scrape_hacker_news(limit=10)
            display_stories(stories)

        elif choice == "2":
            url = input("\nEnter URL to scrape: ").strip()
            title_sel = input("Title CSS selector (default: h2): ").strip() or "h2"
            print(f"\n⏳ Fetching {url}...")
            stories = scrape_generic(url, title_sel)
            display_stories(stories)

        elif choice == "3":
            display_stories(stories)

        elif choice == "4":
            keyword = input("\nEnter keyword to filter: ").strip()
            display_stories(stories, keyword)

        elif choice == "5":
            if not stories:
                print("❌ No stories to save. Scrape something first!")
                continue
            filename = input("Filename (default: headlines.csv): ").strip() or "headlines.csv"
            save_to_csv(stories, filename)

        elif choice == "6":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
