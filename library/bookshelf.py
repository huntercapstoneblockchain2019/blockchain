from . import Book
import user
from random import randint


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
    	id = randint(100,999)
    	return id
    
    def newRequest(self,isbn,user):
    	rid = self.generateRequestId()
    	req_book = self.library[isbn]
    	req_book.addRequest(user)
    	user.addBookRequest(isbn, rid)
    	user.showRequests()
    	print("Request for book successfully made! Here is your Request ID:" + repr(rid))
    	
    def retrieveMessage(self, username):
    	with open('messages.txt', "r") as doc:
    		for message in doc:
    			data = message.split()
    			if username == data[0]:
    				return message
    			else:
    				message = "You currently do not have any messages at this time"
    				return message
    				
    def lookforMessage(self, username):
    	with open('messages.txt', "r") as doc:
    		for message in doc:
    			data = message.split()
    			if username == data[0]:
    				return True
    			else:
    				return False
    
    def createMessage(self, owner, isbn, requestor):
    	with open('messages.txt', "w") as doc:
    		doc.write(repr(owner) + 'you have a request for book with isbn :' + repr(isbn) + 'by user:' +repr(requestor))