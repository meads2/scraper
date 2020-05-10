from bs4 import BeautifulSoup
import pandas as pd


class Parser:
    '''
    Base instance of a generic parser that can parse 
    search engine results from Search Engine results
    pages across major engines.
    '''
    def __init__(self, html, parse_engine='html.parser', engine='google'):
        self.html = str(html)
        self.parse_engine = parse_engine
        self.soup = BeautifulSoup(self.html, self.parse_engine)
        self.engine = engine
        self._results = []

    def _get_results(self):
        '''
        Gets search Results container items from HTML tree
        '''
        # Known mapping css class values of search engine containers
        result_classes = {'google': 'rc',
                          'duck': 'result',
                          'yahoo': '',
                          'bing': ''
                          }
        res = self.soup.find_all(class_=result_classes[self.engine])
        return res

    def _parse_results(self):
        '''
        Parses the search results into clean normalized dictionary
        '''
        res = self._get_results()
        if res is None:
            return None
        else:
            for r in res:
                parsed = {'title': r.find(class_='a').text,
                          'url': r.find(class_='a')['href'],
                          'description': r.find(class_='g').text
                         }
            self._results.append(parsed)
            return parsed

    def to_pandas(self):
        '''
        Generates Pandas dataframe from parsed search results
        '''
        self._parse_results()

        df = pd.DataFrame(self._results)
        return df
     
class GoogleParser(Parser):
    '''
    Instance of particular engine parser
    '''
    pass

class BingParser(Parser):
    '''
    Instance of particular engine parser
    '''
    pass

class YahooParser(Parser):
    '''
    Instance of particular engine parser
    '''
    pass

class DuckDuckGoParser(Parser):
    '''
    Instance of particular engine parser
    '''
    pass