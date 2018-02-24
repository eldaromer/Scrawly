def executeChain(chain, html):
    nodes = []

    for command in chain:
        nodes.append(htmlSearch(html, processHier(command[1])))

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
                if element.name = hier[x]:
                    newPath.append(element)

        path = newPath
        x = x+1
    return path
