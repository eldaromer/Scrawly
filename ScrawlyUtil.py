from urllib.parse import urlparse

def executeChain(chain, html):
    nodes = []

    for command in chain:
        nodes.append(htmlSearch(html, processHier(command[1])))

    return nodes

def processHier(hier):
    return hier.split('/')

#Check whether a url is absolute or not
def isAbsolute(url):
    return bool(urlparse(url).netloc)

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
    return path
