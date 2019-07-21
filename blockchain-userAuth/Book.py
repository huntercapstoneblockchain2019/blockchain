import hashlib
import json
from . import BChain


class Book:
    '''
    The Base Book Class
    '''


    def __init__(self, title, author, genre, isbn, uid):
        self.__bookTitle = title
        self.__bookISBN = isbn
        self.__bookUID = uid
        self.__bookLedger = BChain.BlockChain()
        # In the event that the book has numerous Authors
        if len(author) > 1:
            self.__bookAuthor = ', '.join(author)
        else:
            self.__bookAuthor = author[0]
        # In the event that the book has numerous Genres
        if len(genre) > 1:
            self.__bookGenre = ', '.join(genre)
        else:
            self.__bookGenre = genre[0]

    # Returns all of the Books Information
    def getBookInformation(self):
        print('Book Title:', self.__bookTitle)
        print('Book Author(s):', self.__bookAuthor)
        print('Book Genre(s):', self.__bookGenre)
        print('Book ISBN:', self.__bookISBN)
        print('Book UID:', self.__bookUID)

    # Returns the Genre
    def getGenre(self):
        print(self.__bookGenre)

    # Returns the ISBN
    def getISBN(self):
        return self.__bookISBN

    # Returns Title
    def getTitle(self):
        return self.__bookTitle

    # Returns Author
    def getAuthor(self):
        return self.__bookAuthor

    # Return the Book's BlockChain Transaction History
    def getBookBlockChain(self):
        self.__bookLedger.printChainInfo()

    # Returns the Book's ISBNHashed. Currently Using the Local hash function
    def bookISBNHashed(self):
        return hash(self.__bookISBN)

    # Allows the object to be turned into a string which we can use for encryption

    def __str__(self):
        return self.__bookTitle + '-' + self.__bookAuthor + '-' + self.__bookGenre + '-' + self.__bookISBN + '-' + self.__bookUID
