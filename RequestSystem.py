import Book


class RequestSystem:
    '''
    The Basic Structure of the Request System
    '''
    # Basic Constructor
    def __init__(self):
        self.__Books = {}

    # Addition of a Book to the Request System
    def addBook(self, isbnHash, Book):
        self.__Books[isbnHash] = Book

    # Returns a Count of the amount of Books in the System
    def getAmountofBooks(self):
        print(len(self.__Books))
    
    # Makes a request for a Book
    def requestBookInfo(self, isbn):
        val = hash(isbn)
        return self.__Books[val] #returns book object 

    def newRequest(self,isbn, username)
        rqid = self.generateRequestId()
        book = self.findBook(isbn)
        book.addRequest(username)
        requestor = self.findUser(username)
        requestor.addRequest(isbn, rqid)

    def findUser(username)
        '''
            Searches DB for user and returns the User object
        '''

    def findBook(self,isbn)
        key = hash(isbn)
        return self.__Books[key]

    def generateRequestId(self)
        id= random(3)
        return id
   
    

