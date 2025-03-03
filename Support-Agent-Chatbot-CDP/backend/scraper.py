import requests
from bs4 import BeautifulSoup
import json

docs = {
    "Segment": "https://segment.com/docs/?ref=nav",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

data = {}
for platform, url in docs.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    structured_data = {heading: paragraphs[i] if i < len(paragraphs) else "" for i, heading in enumerate(headings)}
    data[platform] = structured_data

for platform, content in data.items():
    with open(f"data/{platform.lower()}_docs.json", "w") as f:
        json.dump(content, f, indent=4)

print("Scraping completed!")