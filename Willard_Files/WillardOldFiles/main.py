import Block
import BChain
import time
import Book
import hashlib
import RequestSystem


def main():
    myBlockChain = BChain.BlockChain()
    # Books To Be Added To System
    book1 = Book.Book('To Kill A Mockingbird', ['Harper Lee'], [
                      'Novel', 'Bildungsroman', 'Southern Gothic', 'Thriller', 'Domestic Fiction', 'Legal Story'], '978-0446310789', 'B0000000001')
    book2 = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
                      'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
    book3 = Book.Book('The Bad President', ['Donald Trump'], [
                       'Impeachment', 'Delusional'], '978-1sdfasdfasdff', 'B0000000003')

    # Creation of 2 Blocks
    GenesisBlock = Block.Block('0', book1)
    SecondBlock = Block.Block(GenesisBlock.getBlockHash(), book2)

    # Addition of a Block without a Previous Hash of 0
    print('Invalid entry of a non-Genesis Block:')
    myBlockChain.addValidBlock(SecondBlock)

    # Addition of Genesis Block Followed By a Block with an invalid hash
    print()
    BadBlock = Block.Block('asd45234123512341123412362346', book3)
    print('Entry of Valid Block:')
    myBlockChain.addValidBlock(GenesisBlock)

    print('\nAttempt to Add invalid Block to Chain')
    myBlockChain.addValidBlock(BadBlock)

    # Printing of Blockchain
    print('Printing the BChain:')
    myBlockChain.printChainInfo()

    # Tested against an online SHA256 Generator
    # print(hashlib.sha256('Willard'.encode('utf-8')).hexdigest())

    requestInterface = RequestSystem.RequestSystem()
    requestInterface.addBook(book1.bookISBNHashed(), book1)
    requestInterface.getAmountofBooks()
   
   # Requesting a Book
    aBook = requestInterface.requestBookInfo('978-0446310789')
    aBook.getBookInformation()



main()
