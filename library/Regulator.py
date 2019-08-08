from . import BChain
from . import Book
from . import Block
from . import bookshelf
from . import Transaction
import csv


class Regulator:

	__masterLedger= {}

	def __init__(self, request_id, user, isbn,location, book):
		self.rid = request_id
		self.user = user
		self.isbn = isbn
		self.location = location
		self.book =book


	
		
	'''
		def validation(self, isbn, rid, pblock):
		blckchain= self.__masterLedger[isbn]
		lastKey = (blckchain.lastblock()).getBlockHash()
		validBlock= block.Block(lastKey,rid)
		
		if pblock.getBlockHash() == validBlock.getBlockHash()
			self._addTransaction(isbn, pblock)
			return true
		else 
			return false
	'''
	
	def addTransaction(self,hisbn, nblock, book):
		book.addValidBlock(nblock)
		self.__updateLedger(hisbn, book.getBookBlockChain())
		
	
	def __updateLedger(self, hisbn, nbchain):
		self.__masterLedger[hisbn] = nbchain
		
		
	def ledgerImport(self):
		ledger = open('masterLedger.csv')
		ml = csv.reader(ledger)
		
	def createtransactionBlock(self):
		blockchain_info = self.book.getBookBlockChain()

		if blockchain_info.__str__() == "Chain is Empty":
			previousHash=0
			lastblockOwnner = "None"
			block = Block.Block(previousHash, Transaction.Transaction(self.rid, lastblockOwnner, self.user, self.isbn, self.location))

		else:
			lastblockOwnner = blockchain_info.last_blockowner()
			previousHash = blockchain_info.last_block().getPreviousHash()
			block = Block.Block(previousHash, Transaction.Transaction(self.rid, lastblockOwnner, self.user, self.isbn, self.location))

		self.addTransaction(self.isbn, block, self.book)
		print(self.__masterLedger[self.isbn].__str__())


