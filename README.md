![](docs/Artboard.png)
![GitHub All Releases](https://img.shields.io/github/downloads/meads2/scraper/total)
![GitHub last commit](https://img.shields.io/github/last-commit/meads2/scraper)

## Scraper
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

####  **3. Enter search terms to scrape results**
```bash
python scraper --terms 'my favorite team'
```

You can use additional flags for various functionality if desired, some default assumptions are assumed.

#### **Parameters**

**--terms** - String value of search terms to pass to scraper engine. (Must be quote encapsalated)

**--screenshot** - Defaults to False. If present selenium will take a screenshot of browser search window

**--dest** - Defaults to user's download. If specified will save results to defined location

**--silent** - Defaults to True. If false, browser window will open at runtime to see execution, useful for debugging.

### **Examples**

#### **Basic Example**
```bash
python scraper --terms 'daily news near me'
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