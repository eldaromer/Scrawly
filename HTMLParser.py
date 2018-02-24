import requests
from lxml import html

def getHTMLObject(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree



def main():
    page = getHTMLObject('https://boulder.craigslist.org/')
    print html.tostring(page)



main()
