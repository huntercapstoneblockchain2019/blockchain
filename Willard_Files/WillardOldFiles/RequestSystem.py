import Book
# These are the books to initialize the system
book1 = Book.Book('To Kill A Mockingbird', ['Harper Lee'], [
    'Novel', 'Bildungsroman', 'Southern Gothic', 'Thriller', 'Domestic Fiction', 'Legal Story'], '978-0446310789', 'B0000000001')
book2 = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
    'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
book3 = Book.Book('The Bad President', ['Donald Trump'], [
    'Impeachment', 'Delusional'], '978-198782321843', 'B0000000003')


class RequestSystem:
    '''
    The Basic Structure of the Request System
    '''
    
    # Basic Constructor

    def __init__(self):
        self.__Books = {}
        self.__Books.update({'978-0446310789': book1, '978-1451697216':book2, '978-198782321843': book3})
        self.__loginCredentials = {'admin' : ['admin123', '98765'], 'willJ': ['pass123', '12345']}

    # Addition of a Book to the Request System
    def addBook(self, isbnHash, Book):
        self.__Books[isbnHash] = Book

    # Addition of a Book by a User
    def userAddBook(self):
        loginBool = False
        print('To Add a Book to The Library System, you must be a registered User... Please Login')
        userId = input('User Name: ')
        passWord = input('Password: ')

        if userId in self.__loginCredentials:
            if passWord == self.__loginCredentials[userId][0]:
                print('Success!!')
                loginBool = True
            else:
                print('Invalid Credentials')
        else:
            print('Invalid Credentials')        


        if loginBool == True:
            isbn = input('Enter the books ISBN: ')
            title = input('Enter the books Complete Title: ')
            author = input('Enter the Author(s) of the book (Separate by comma, for multiple): ')
            authorList = author.split(',')
            genre = input('Enter the books genre (Separate by comma, for multiple): ')
            genreList = genre.split(',')
            # Create a variable, that would store the current user, therefore the new book
            # will have a currentuser or maybe a variable called owner
            uid = str(len(self.__Books) + 1)
            newBook = Book.Book(title, authorList, genreList, isbn, uid)
            self.addBook(isbn, newBook)
        else:
            print('\nHTTP ERROR 401: UNAUTHORIZED\n')

    # Returns a Count of the amount of Books in the System
    def getAmountofBooks(self):
        print('There are a total of ', len(self.__Books), 'Book(s) in the System.')

    # Makes a request for a Book
    def requestBookInfo(self, isbn):
        val = hash(isbn)
        try:
            return self.__Books[val]
        except KeyError:
            # print(str(k))
            print('Not a valid ISBN')

    # Returns the list of Users
    def listOfSystemUsers(self):
        for x in self.__loginCredentials:
            print(x)

    # Returns al the Books in the System along with their user
    def booksOfTheSystem(self):
        count = 1
        
        if len(self.__Books) == 0:
            print('***System Currently has no books***')
        else:
            for isbn, books in self.__Books.items():
                print()
                print('Book', count)
                # print("Isbn Hash:", isbn)
                books.getBookInformation()
                count += 1

    # Get the books current Status
    def booksCurrentStatus(self):
        isbn = input('Please Enter the ISBN of the Book you are Researching: ')
        self.__Books[isbn].getBookStatus()
    def mainLoop(self):
        print('''
        Welcome to The Request System Portal:
        
        [1] - User Lookup
        [2] - All Books
        [3] - Add Books
        [4] - Amount of Books in System
        [5] - Book Status
        [6] - Exit
        
        ''')
        # Request Book Need To be Added
        # Book Status May have to use or access the books Blockchain

        action = input('\tWhat Would You Like to do? (Enter a Value) ')

        if action == '1':
            self.listOfSystemUsers()
        elif action == '2':
            self.booksOfTheSystem()
        elif action == '3':
            self.userAddBook()
        elif action == '4':
            self.getAmountofBooks()
        elif action == '5':
            self.booksCurrentStatus()
        elif action == '6':
            print('Exiting Request System... Goodbye!\n')
            exit()
        else:
            print('Invalid Entry')

