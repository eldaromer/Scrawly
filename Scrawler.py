import HTMLObjectify
import ScrawlyUtil

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

		# Initiate request to HTMLObjectify for original url and get parsed/preprocessed object back

		self.html = HTMLObjectify.getHTMLObject(self.rootUrl)


		nodes = ScrawlyUtil.executeChain(self.commandChain, self.rootUrl)

		for nodeList in nodes:
			for node in nodeList:
				print(node.text)


	def addToChain(self, func, hier):
		self.commandChain.append([func, hier])

	def printChain(self):
		for x in range(len(self.commandChain)):
			print ("func: " + self.commandChain[x][0] + " | arg: " + self.commandChain[x][1])