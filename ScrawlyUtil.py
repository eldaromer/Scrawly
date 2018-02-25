from urllib.parse import urlparse
import HTMLObjectify

#Execute the chain of scrapes known as a "Scrawl"
#Omer just thinks that the word "chain" is hot shit 
def executeChain(chain, url):

    nodes = []
    htmls = [HTMLObjectify.getHTMLObject(url)]
    links = [url]
    
    #Loop through the commands in the chain
    for command in chain:
        #Check whether the command is for scraping a link or for scraping content
        if command[0] == 'content':
            for html in htmls:
                nodes.append(htmlSearch(html, processHier(command[1])))
        elif command[0] == 'link':
            
            #Scrape all of the links at the current heigherarchy
            newLinks = []
            newHtmls = []
            
            for x in range(len(htmls)):
                checkLinks = htmlSearch(htmls[x], processHier(command[1]))
                for link in checkLinks:
                    link = link.get('href')
                    link = constructLink(links[x], link)
                    newLinks.append(link)
                    newHtmls.append(HTMLObjectify.getHTMLObject(link))

            htmls = newHtmls
            links = newLinks

    return nodes

#Split the heigherarchy command by a / character
def processHier(hier):
    return hier.split('/')

#Check whether a url is absolute or not
def isAbsolute(url):
    return bool(urlparse(url).netloc)

#Construct a full URL for the next jump in the crawl
def constructLink(currentUrl, nextUrl):
    #Verify the format of the next URL
    if isAbsolute(nextUrl):
        #URL is absolute and doesn't need reconstruction
        return nextUrl
    else:
        #URL is not absolute, reconstruct it from the relative url and the domain
        #Start by getting the domain from the old URL
        parsed_old_uri = urlparse(currentUrl)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_old_uri)
        
        #Check for a single ../
        if nextUrl[:3] == '../':

            return currentUrl + '/' + nextUrl
        else:
            if nextUrl[0] == '/':
                return domain + nextUrl
            else:
                return domain + '/' + nextUrl

#Creates the heigherarchy path for a given element
def traceElement(element):
    currentParent = element.parent
    elementPath = element.name

    while currentParent != 'html':
        elementPath = element.parent.name + '/'  + elementPath
        element = element.parent
        currentParent = element.parent.name
    
    return elementPath

#Grab the first element by the specified class
def getElementByClass(className, html):
    found = html.find_all(class_=className, limit=1)
    return found[0]

#Gets the elements in html at a specified heigerarchy
def htmlSearch(html, hier):
    path = []

    for element in html.html.children:
        if element.name == hier[0]:
            path.append(element)

    x = 1
    while path != [] and x < len(hier):
        newPath = []

        for item in path:
            for element in item.children:
                if element.name == hier[x]:
                    newPath.append(element)

        path = newPath
        x = x+1

    for element in path:
        print(element.text)

    return path
