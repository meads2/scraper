from scraper.browser import get_screenshot, get_html
from scraper.search import create_site_combinations, create_search_url, create_audit_url
from scraper.parsers import Parser, GoogleParser

from tqdm import tqdm
import time
import click
from pathlib import Path

USERS_DOWNLOAD=Path.cwd()


@click.command()
@click.argument('terms')
@click.option('--showme', default = True, help = 'True false value to control whether browser opens.(Defaults to true, browser hidden)')
@click.option('--dest', default = USERS_DOWNLOAD, help = 'Destination to save result files to.(Defaults to users downloads')
@click.option('--selfie', default = False, help = 'If passed, takes a screenshot of search results. Useful for debugging.')
def main(terms, showme, dest, selfie):
    '''
    Web scraping search engine results made easy.
    Get the first page results of your search in
    a nice dataframe.
    '''
    click.echo(f'Search for: {terms}')
    
    url = create_search_url(terms)
    print(url)
    html = get_html(url)

    prsr = Parser(html)
    df = prsr.to_pandas()
    print(df)
    
if __name__ == '__main__':
    main()