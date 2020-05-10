![](docs/Artboard.png)
![GitHub All Releases](https://img.shields.io/github/downloads/meads2/scraper/total)
![GitHub last commit](https://img.shields.io/github/last-commit/meads2/scraper)

A library for performing simple web scraping of a search engine's results page for data analysis tasks. (Note: For personal non-commercial use only. Follow all web scraping guidelines, before getting started. Be kind to servers.)

### **Getting Started**
This library is intended for personal use only to get search results from a search engine for downstream analysis. 

#### **1. Create Folder**
```bash
mkdir scraper && cd scraper
```

#### **2. Clone Project Repo**
```bash
python -m venv venv
source venv/bin/activate
git clone https://github.com/meads2/scraper.git
pip install
```

#### **3. Enter search terms to scrape results**
```bash
python scraper --terms 'my favorite team'
```

#### **4. Check downloads folder for screenshot and file**
This application saves the scraped web results to a users download folder along with a screenshot of search performed for review and debugging if necessary.

### **Features**