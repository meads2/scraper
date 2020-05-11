![](docs/Artboard.png)
![GitHub All Releases](https://img.shields.io/github/downloads/meads2/scraper/total)
![GitHub last commit](https://img.shields.io/github/last-commit/meads2/scraper)
![Python](https://img.shields.io/badge/Python-3.0-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Stars)](https://github.com/meads2/scraper)
[![Sourcegraph for Repo Reference Count](https://img.shields.io/sourcegraph/rrc/github.com/gorilla/mux.svg)](https://github.com/meads2/scraper)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/badges/shields.svg)](https://github.com/meads2/scraper)
[![Codacy grade](https://img.shields.io/codacy/grade/e27821fb6289410b8f58338c7e0bc686.svg)](https://github.com/meads2/scraper)

## Scraper
A library for performing simple web scraping of a search engine's results page for data analysis tasks. *(Note: For personal non-commercial use only. Follow all web scraping guidelines, before getting started. Be kind to servers.)*

> Requies Python version 3.6 or greater.

### **Getting Started**
This library is intended for personal use only to get search results from a search engine for downstream analysis. 

#### **1. Clone Project Repo**
```bash
git clone https://github.com/meads2/scraper.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pwd
```

####  **2. Enter search terms to scrape results**
```bash
python scraper --terms 'my favorite team'
```

You can use additional flags for various functionality if desired, some default assumptions are assumed.

#### **Parameters**

**--terms** - String value of search terms to pass to scraper engine. (Must be quote encapsalated)

**--selfie** - If present selenium will take a screenshot of the browser search window returned.

**--dest** - If specified will save results to defined location

**--showme** - If present browser window will open at runtime to see execution, useful for debugging.

**--engine** - If specified will use that search engine, defaults to Google. ['Bing' - Microsoft Bing, 'duck' - DuckDuckGo, 'google' - Google, 'Yahoo'-Yahoo]
### **Examples**

#### **Basic Example**
```bash
python scraper --terms 'daily news near me'
### ... running and scraping quietly
### Check your downloads for a surprise!
```

#### **Screenshot Example**
```bash
python scraper --terms 'daily news near me' --selfie
### ... running and scraping quietly
### Check your downloads for a surprise!
```

#### **Verbose Example**
```bash
python scraper --terms 'daily news near me' --showme 
### ... running and scraping right before your eyes
### Check your downloads for a surprise
```

#### **Custom Save Example**
```bash
python scraper --terms 'daily news near me' --dest '../some/location/'
### ... running and scraping quietly to your defined location
### Check your downloads for a surprise!
```