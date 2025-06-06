import requests
from bs4 import BeautifulSoup


def fetch_latest_articles(limit=3):
    """Fetch the latest articles from Al Jazeera RSS feed."""
    feed_url = "https://www.aljazeera.com/xml/rss/all.xml"
    response = requests.get(feed_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")[:limit]
    articles = []
    for item in items:
        title = item.title.text.strip() if item.title else ""
        link = item.link.text.strip() if item.link else ""
        pub_date = item.pubDate.text.strip() if item.pubDate else ""
        articles.append({"title": title, "link": link, "pub_date": pub_date})

    return articles


def main():
    articles = fetch_latest_articles(3)
    for idx, art in enumerate(articles, 1):
        print(f"{idx}. {art['title']} ({art['pub_date']})")
        print(art['link'])
        print()


if __name__ == "__main__":
    main()
