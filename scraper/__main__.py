from scraper.browser import get_screenshot, get_html
from scraper.search import create_site_combinations, create_search_url, create_audit_url
from tqdm import tqdm
import time
import click

@click.command('scraper')
@click.option('--terms', default='weather near me', help='The search terms to pass to search engine')
@click.option('--silent', default=True, help='True false value to control whether browser opens.(Defaults to true, browser hidden)')
@click.option('--dest', default=None, help='Destination to save result files to.(Defaults to users downloads')

def main(terms):
    click.echo(terms)
    
if __name__ == '__main__':
    main()