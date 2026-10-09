# 🌐 Natural Language Processing (NLP) & Web Scraping

This directory contains coursework and web scraping pipelines developed for gathering unstructured natural language datasets during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 📁 Directory Structure

```text
NLP/
└── Assignment 01 – Scraping News Articles/
    ├── sol_01.py                           # Automated web scraper using BeautifulSoup & requests
    ├── Vishal_Indian_express_news.csv      # Scraped dataset with metadata and full article text
    └── Scraping News Articles.pdf          # Assignment problem statement & requirements
```

---

## 🔍 Overview: Indian Express News Scraper

### Objective
To build an automated, fault-tolerant Python crawler capable of fetching news article URLs from *The Indian Express* homepage and extracting clean article bodies for subsequent NLP analysis (topic modeling, sentiment analysis, and summarization).

### Technical Workflow
1. **HTTP Request Session**: Uses custom user-agent headers to mimic modern browser requests and bypass basic anti-scraping filters.
2. **Link Discovery**: Inspects `h1`, `h2`, and `h3` header tags using `BeautifulSoup` to locate verified news links matching `/article/` routing patterns while maintaining a uniqueness `set` to eliminate duplicate URLs.
3. **Deep Content Extraction**: Visits each targeted article link, extracts title, author/intern tagging, and locates full article text inside the primary `.story_details` DOM container.
4. **Rate Limiting & Exception Handling**: Includes a 1-second polite request delay between queries and graceful exception recovery for timeouts and HTTP errors.
5. **Structured Export**: Compiles extracted articles into a pandas `DataFrame` and exports them to `Vishal_Indian_express_news.csv`.

---

## 📊 Dataset Schema

| Column Name | Description |
|---|---|
| `NEWS_TITLE` | Headline of the news article |
| `Intern Name` | Submitter identifier (`Vishal Singh`) |
| `NEWS_LINK` | Canonical web URL of the original article |
| `FULL_SCRAPED_TEXT` | Cleaned textual content extracted from article body |

---

## 🚀 How to Run

```bash
python "NLP/Assignment 01 – Scraping News Articles/sol_01.py"
```
*(Note: Requires active internet connectivity to contact `indianexpress.com`)*

