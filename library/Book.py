import hashlib
import queue
import json
from . import BChain
from . import Block



class Book:

	request_queue = queue.Queue()

	def __init__(self, title, author, genre, isbn, uid):
		self.__bookTitle = title
		self.__bookISBN = isbn
		self.__bookUID = uid
		self.__bookLedger = BChain.BlockChain()
		# In the event that the book has numerous Authors
		if len(author) > 1:
			self.__bookAuthor = ', '.join(author)
		else:
			self.__bookAuthor = author[0]
		# In the event that the book has numerous Genres
		if len(genre) > 1:
			self.__bookGenre = ', '.join(genre)
		else:
			self.__bookGenre = genre[0]
		
		self.unconfirmed_transactions = []
        #self.BlockChain = []

	# Returns all of the Books Information
	def getBookInformation(self):
		print('Book Title:', self.__bookTitle)
		print('Book Author(s):', self.__bookAuthor)
		print('Book Genre(s):', self.__bookGenre)
		print('Book ISBN:', self.__bookISBN)
		print('Book UID:', self.__bookUID)

	def getStringBookInformation(self):
		return ('Book Title:' + self.__bookTitle + '\n' + 'Book Author(s):' + self.__bookAuthor + '\n' + 'Book Genre(s):' + self.__bookGenre + '\n' + 'Book ISBN:' + self.__bookISBN + '\n' + 'Book UID:' + self.__bookUID + '\n')
		   

	# Returns the Genre
	def getGenre(self):
		print(self.__bookGenre)

	# Returns the ISBN
	def getISBN(self):
		return self.__bookISBN

	# Returns Title
	def getTitle(self):
		return self.__bookTitle

	# Returns Author
	def getAuthor(self):
		return self.__bookAuthor

	# Return the Book's BlockChain Transaction History
	def getBookBlockChain(self):
		return self.__bookLedger

	# Returns the Book's ISBNHashed. Currently Using the Local hash function
	def bookISBNHashed(self):
		return hash(self.__bookISBN)

	#adds new request to queue
	def addRequest(self, user):
		self.request_queue.put(user)

	#retrieves next request in queue
	def getNextRequest(self):
		return self.request_queue.get()
	
	def getAllRequests(self):
		for req in request_queue:
			print (req)

	# Allows the object to be turned into a string which we can use for encryption
	def __str__(self):
		return self.__bookTitle + '-' + self.__bookAuthor + '-' + self.__bookGenre + '-' + self.__bookISBN + '-' + self.__bookUID

	def addValidBlocks(self, BlockExample):
		#print(BlockExample.__str__().getTra)

		self.__bookLedger.addBlock(BlockExample)
		print(self.__bookLedger.getBlockCount())

		#print(self.__bookLedger.__str__())
		#return self.__bookLedger.addBlock(BlockExample)



	def getlastOwner(self):
		block = BChain.BlockChain.last_block()
		block.getOwner()

	def rest(self, blockchain):
		self.__bookLedger = blockchain

		saveFile = open("Newdata.txt", 'w')

		saveFile.write(blockchain.__str__())

		# writes the text contained in the variable writeMe to the file declared above
		# Always remember after an operation is completed to close it.
		saveFile.close()

