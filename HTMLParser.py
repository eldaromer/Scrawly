import requests
from lxml import html

def getHTMLObject(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree

def printPage(page):
    for element in page.iter():
        print("%s - %s" % (element.tag, element.text))


def main():
    page = getHTMLObject('https://boulder.craigslist.org/')
    printPage(page)


main()
