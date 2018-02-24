import requests
from bs4 import BeautifulSoup
import html.parser

def getHTMLObject(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def main():
    page = getHTMLObject('https://boulder.craigslist.org/')
    print(page.prettify())



main()
