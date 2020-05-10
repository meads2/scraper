from bs4 import BeautifulSoup
import lxml

class Parser:
    '''
    Base instance of a generic parser that can parse 
    search engine results from Search Engine results
    pages across major engines.
    '''
    def __init__(self, html, parser='html.parser', engine='google'):
        self.html = html
        self.soup = BeautifulSoup(html, parser)
        self.engine = engine
    
    def get_results(self):
        res = self.soup.find_all(class_='rc')
    
class GoogleParser(Parser):
    pass

class BingParser(Parser):
    pass

class YahooParser(Parser):
    pass

class DuckDuckGoParser(Parser):
    pass