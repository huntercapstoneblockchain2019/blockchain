from . import BChain
from . import Book
from . import Block
from . import bookshelf


class Regulator:

	__masterLedger= {}
	
	def validation(self, isbn, rid, pblock):
		blckchain= self.__masterLedger[isbn]
		lastKey = (blckchain.lastblock()).getBlockHash()
		validBlock= block.Block(lastKey,rid)
		
		if pblock.getBlockHash() == validBlock.getBlockHash()
			self._addTransaction(isbn, pblock)
			return true
		else 
			return false
	
	def addTransaction(self,hisbn, nblock, book):
		book.addtoBlockChain(nblock)
		self.__updateLedger(hisbn, book.getBlockChain())
		
	
	def __updateLedger(self, hisbn, nbchain):
		self.__masterLedger[hisbn] = nbchain
		
		
	def ledgerImport(self):
		ledger = open('masterLedger.csv')
		ml = csv.reader(ledger)
		
		
	
		
	
	
	

