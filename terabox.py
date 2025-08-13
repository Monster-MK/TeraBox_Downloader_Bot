import requests
import cloudscraper

def get_direct_link(url):
    scraper = cloudscraper.create_scraper()
    res = scraper.get(url)
    if res.status_code != 200:
        raise Exception("Failed to fetch page.")
    # இங்கு HTML parse பண்ணி real download link எடுக்கணும்
    # Example placeholder:
    return "https://example.com/download/file.mp4"
