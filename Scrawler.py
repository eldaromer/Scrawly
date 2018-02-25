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
			print ("4. Quit")
			choice = int(input("Input your decision:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
			print ("\n")

			if choice == 1:
				hier = input ("Please input your link hierarchy\n")
				self.addToChain("link", hier, None)
				print("\n\n")
			elif choice == 2:
				hier = input ("Please input your content hierarchy\n")
				variable = input("Please input what you want to name this variable\n")
				self.addToChain("content", hier, variable)
				print("\n\n")
			elif choice == 3:
				quit = True
				self.run()
			elif choice == 4:
				quit = True
			else:
				print ("Invalid choice, try again")

	

	def run(self):

		self.printChain()

		# Initiate request to HTMLObjectify for original url and get parsed/preprocessed object back

		self.html = HTMLObjectify.getHTMLObject(self.rootUrl)


		nodes = ScrawlyUtil.executeChain(self.commandChain, self.rootUrl, self.html)



		for keys,values in nodes.items():
			print(keys)
			print(values)


	def addToChain(self, func, hier, variable):
		self.commandChain.append([func, hier, variable])

	def printChain(self):
		for x in range(len(self.commandChain)):
			print ("func: " + self.commandChain[x][0] + " | arg: " + self.commandChain[x][1])