import HTMLObjectify

def executeChain(chain, url):
    nodes = []
    htmls = [HTMLObjectify.getHTMLObject(url)]
    links = [url]

    for command in chain:
        if command[0] == 'content':
            for html in htmls:
                nodes.append(htmlSearch(html, processHier(command[1])))
        elif command[0] == 'link':

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

def processHier(hier):
    return hier.split('/')

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
