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


    def createrequest(self):

        tx_data = request.get_json()
        required_fields = ["author", "bookName", "requestCreator"]
        for field in required_fields:
            if not tx_data.get(field):
                return "Invlaid transaction data", 404

        tx_data["timestamp"] = time.time()


        transaction.new_transaction(tx_data)

        return "Success", 201