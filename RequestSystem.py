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
        return self.__Books[val]

     def newRequest(self,isbn, user)
        rqid = self.generateRequestId()
        book = self.findBook(isbn)
        book.addRequest(user.getUserName())
        user.addRequest(isbn, rqid)


    def findBook(self,isbn)
        key = hash(isbn)
        return self.__Books[key]

    def generateRequestId(self)
        id= random(3)
        return id
