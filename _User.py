import BChain
import Block


class User():

	book_requests = {}
	book_ledger = {}
	
	#Constructor
	def __init__(self, uname)
		self.username = uname
	
	#Accessor Function		
	def getUsername(self)
		return self.username
	
	#Adds a new request to user's dictionary of requests	
	def addBookRequest(self, isbn, rqid)
		self.book_requests[isbn] = rqid
	
	#Returns the request id of a given book 	
	def getRequestId(self, isbn)
		if isbn in book_requests
			return self.book_requests[isbn]
		else 
			print ("No record of request for this book")
			return None

	
	#Used to update user's book_ledger
	def updateLedger(self, mledger)
		self.book_ledger = mledger
	
	#Returns the book's corresponding block chain
	def getBookChain(self, isbn)
		if isbn in book_ledger	
			return book_ledger[isbn]
		else 
			print ("Record of book does not exist!")
			return None
	
	#Given the request id as a parameter and the book's isbn a transaction block 
	# is created and returned by user 
	def createTransactionBlock(self, req_id, isbn)
		blk_chain = self.getBookChain(isbn) # get corresponding blockchain for book with isbn
		prev_blk = blk_chain.last_block()
		trans_block = block.Block(prev_blk.getBlockHash(), req_id)
		return trans_block
	
		
	