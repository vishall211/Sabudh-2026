import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://indianexpress.com/"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    # Open the Indian Express homepage
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    news = []
    links = set()

    # Find news headlines on the homepage
    for heading in soup.find_all(["h1", "h2", "h3"]):
        a = heading.find("a")
        if a:
            title = a.get_text(strip=True)
            link = a.get("href")

            if link and "/article/" in link and link not in links:
                links.add(link)
                news.append({
                    "title": title,
                    "link": link
                })

        # We need 20 to 30 news articles
        if len(news) >= 30:
            break

    articles = []

    # Open each news article
    print("\n –––– Starting Scrapping News Article –––––\n")
    for i, item in enumerate(news):

        try:
            print("Scraping article ", i + 1)
            response = requests.get(
                item["link"],
                headers=headers,
                timeout=10
            )
            
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the main article text
            article = soup.find("div", class_="story_details")

            if article:
                text = article.get_text(" ", strip=True)
            else:
                text = "Opps!! Article text not found."

            articles.append({
                "NEWS_TITLE": item["title"],
                "Intern Name": "Vishal Singh",
                "NEWS_LINK": item["link"],
                "FULL_SCRAPED_TEXT": text
            })

            # Wait for a second before the next request
            time.sleep(1)

        except requests.RequestException:
            print("\nCould not scrape this article.")

    # Create DataFrame
    df = pd.DataFrame(articles)

    # Save the data into CSV
    df.to_csv("NLP/Assignment 01 – Scraping News Articles/Vishal_Indian_express_news.csv", index=False)

    print("\n –––– Task Completed Successfully :) –––––\n")
    print("\nTotal articles : ", len(df),"\n")

except requests.RequestException:
    print("\nppss !! Could not connect to the Indian Express website.\n")