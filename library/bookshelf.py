from . import Book
#import user
import random


class Bookshelf:

    library={}

    #Initialization of object with possibility of adding genre
    def __init__(self,genre=None):
        self.genre = genre

    #Adds a book to the shelf
    def addBook(self,book): 
        self.library[book.getISBN()] = book
        
    #Returns book object    
    def getBook(self, isbn):
    	return self.library[isbn]
    
    '''
    #Return current book owner
    def getOwner(self, isbn):
    	book = self.getBook(isbn)
	#How is the user stored in the block? username, user id
    '''	
    
    def generateRequestId(self):
    	id = random(3)
    	return id
    
    def newRequest(self,isbn,user):
    	rid = self.generateRequestId()
    	req_book = self.library[isbn]
    	req_book.addRequest(user.getUsername())
    	print("Request for book successfully made! Here is your Request ID:" + rid)

	
 
 		
   

        






