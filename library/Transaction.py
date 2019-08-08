
from random import randint
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
        return 'Request ID: ' + self.__requestId.__str__() + '\nLenders ID: ' + self.__lenderUserId.__str__() + '\nBorrowers ID: ' + self.__borrowerUserId.__str__() + '\nBooks ID: ' + self.__booksISBN.__str__() + '\nMeet Up Location: ' + self.__meetUpLocation

    def getNewOwner(self):
        return self.__borrowerUserId
