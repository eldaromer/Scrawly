#import HTMLParser

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

		#this.currentPage = HTMLParser.get(this.rootUrl)

		# Display the preprocessed html to the user

		# Capture any input from the webpage and add to the command chain

		# Wait for done command

		# Pass command chaining to IterativeProcessor

	def addToChain(self, func, hier):
		self.commandChain.append([func, hier])

	def printChain(self):
		for x in range(len(self.commandChain)):
			print ("func: " + self.commandChain[x][0] + " | arg: " + self.commandChain[x][1])