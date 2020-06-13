import itertools as it
import urllib.parse as url


def create_site_combinations(list1, list2):
    '''
    Creates a unique list of all url combinations for
    2 iterable lists

    Params:
        list1 - list of term set 1
        list2 - list of term set 2
    
    Returns:
        combos - list of tuples containing site, filetype
    '''
    combos = [*it.product(list1, list2)]

    return combos

def create_search_url(search_term, engine='google'):
    '''
    Creates a browser ready search url with passed parameters

    Params:
        combos - Tuple Pair of (site, filetype) as strings to create url
        engine - string of search engine ['google'|'duck'|'bing'|'yahoo']

    Return:
        url - search ready URLS
    '''
    query = {'q': f'{search_term}'}

    qry_safe = url.urlencode(query)

    search_engines = {
        'google': 'https://www.google.com/search?',
        'duck': 'duckduckgo.com/?',
        'yahoo': 'yahoo.com/?',
        'bing': 'bing.com/?'
    }

    url_safe = f'{search_engines[engine]}{qry_safe}'
    return url_safe

def create_audit_url(combo, engine='google'):
    '''
    Creates a URL for search engine "hacking" to look
    at a certain file types public exposure on a domain
    '''
    hack_terms = {'google': ['site', 'filetype'],
                  'duck': ['website', 'filetype'],
                  'yahoo': ['website', 'filetype'],
                  'bing': ['website', 'filetype']
                  }

    query = {'q': f'{hack_terms[engine][0]}:{combo[0]} {hack_terms[engine][1]}:{combo[1]}'}

    qry_safe = url.urlencode(query)

    search_engines = {
        'google': 'https://www.google.com/search?',
        'duck': 'duckduckgo.com/?',
        'yahoo': 'yahoo.com/?',
        'bing': 'bing.com/?'
    }

    url_safe = f'{search_engines[engine]}{qry_safe}'
    return url_safe
