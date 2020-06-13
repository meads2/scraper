import selenium.webdriver as sel
from pathlib import Path

DRIVER_PATH=Path.cwd().joinpath('chromedriver')

def get_html(url):
    '''
    Returns HTML page source of a browser rendered
    website for downstream parsing.
    '''
    options = sel.ChromeOptions()  
    options.add_argument('headless')
    browser = sel.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
    browser.get(url)
    html = browser.page_source
    return html

def get_screenshot(url):
    '''
    Takes a PNG screenshot of given URL. Useful for debugging
    parsing errors associated with certain URL requests to 
    train parsers.
    '''
    options = sel.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('start-maximized')
    browser = sel.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
    browser.get(url)
    img = browser.get_screenshot_as_file('./img.png')
    return img