class Transaction:
    '''
    The Base Transaction Class
    '''

    def __init__(self, reqId, oldId, newUserId, bkISBN, location):
        self.__requestId = reqId
        self.__lenderUserId = oldId
        self.__borrowerUserId = newUserId
        self.__booksISBN = bkISBN
        self.__meetUpLocation = location
    
    def transactionDetails(self):
        return 'Request ID: ' + self.__requestId + '\nLenders ID: ' + self.__lenderUserId + '\nBorrowers ID: ' + self.__borrowerUserId + '\nBooks ID: ' + self.__booksISBN + '\nMeet Up Location: ' + self.__meetUpLocation