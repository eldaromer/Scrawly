import HTMLParser

class Scrawler:
	def __init__(self, url):

		self.rootUrl = url
		print(url)
		self.commandChain = []

	def interactive(self):
		quit = False


		print ("Welcome to your interactive buddy Scrawly!\nThese are your options:\n\n")

		while not quit:
			print ("1. Select link to scrape")
			print ("2. Select content to scrape")
			print ("3. Run")
			choice = int(input("Input your decision:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"))

			if choice == 1:
				hier = input ("Please input your link hierarchy\n")
				self.addToChain("link", hier)
				print("\n\n")
			elif choice == 2:
				hier = input ("Please input your content hierarchy\n")
				self.addToChain("content", hier)
				print("\n\n")
			elif choice == 3:
				quit = True
				self.run()
			else:
				print ("Invalid choice, try again")

	

	def run(self):

		self.printChain()

		# Initiate request to HTMLParser for original url and get parsed/preprocessed object back

		self.html = HTMLParser.getHTMLObject(self.rootUrl)

		nodes = []

		for x in range(len(self.commandChain)):
			nodes.append(self.htmlSearch(self.html, self.processHier(self.commandChain[x][1])))

		for nodeList in nodes:
			for node in nodeList:
				print(node.string)


	def addToChain(self, func, hier):
		self.commandChain.append([func, hier])

	def printChain(self):
		for x in range(len(self.commandChain)):
			print ("func: " + self.commandChain[x][0] + " | arg: " + self.commandChain[x][1])

	def processHier(self, hier):
		return hier.split('/')

	def htmlSearch(self, html, hier):

		path = []

		for element in html.html.children:
			if element.name == hier[0]:
				path.append(element)


		x = 1
		while path != [] and x < len(hier):
			newPath = []

			for thing in path:
				for element in thing.children:
					if element.name == hier[x]:
						newPath.append(element)

			path = newPath
			x = x+1

		return path

		