from flask import Flask, render_template, request,url_for,session,redirect
from flask import send_file

#from . import create_app
from library import bookshelf
from library import Book
from user import User, app, db
import password as p
from library import Block
from library import Transaction

import os
# app= Flask(__name__)
# app=create_app()
db.create_all()
app.secret_key = os.urandom(16)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



shelf = bookshelf.Bookshelf()
@app.route('/')
def index():
    if 'username' in session:

        #shelf=Bookshelf()

        book1 = Book.Book('To Kill A Mockingbird', ['Harper Lee'], [
            'Novel', 'Bildungsroman', 'Southern Gothic', 'Thriller', 'Domestic Fiction', 'Legal Story'], '978-0446310789', 'B0000000001')
        book2 = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
            'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
        book3 = Book.Book('The Bad President', ['Donald Trump'], [
            'Impeachment', 'Delusional'], '978-1sdfasdfasdff', 'B0000000003')

       
        
        # Adds a Book into the shelf
        shelf.addBook(book1)
        shelf.addBook(book2)
        shelf.addBook(book3)
        # print(shelf.index[book.getISBN()])

        # Hard Coded Transactions for Book 1
        HCT1 = Transaction.Transaction(
        '12345', 'User01', 'User02', '978-0446310789', 'Brooklyn Bridge Park')
        HCT2 = Transaction.Transaction(
        '76483', 'User02', 'User03', '978-0446310789', 'Hunter College Lunchroom')

        # Hard Coded Transactions for Book 2
        HCT3 = Transaction.Transaction(
        '0', 'User04', 'User06', '978-1451697216', 'Central Park - North Corridor')
        # HCT4 = Transaction.Transaction('85274', 'User06', 'User03', '978-1451697216', 'Prospect Park')

        # Addition of Hard coded Block Transactions for Book 1
        GenBlock = Block.Block('0', HCT1)
        SecondBlock = Block.Block(GenBlock.getBlockHash(), HCT2)
        GenBlockBook2 = Block.Block('0', HCT3)

        book1.addValidBlock(GenBlock)
        book1.addValidBlock(SecondBlock)
        book2.addValidBlock(GenBlockBook2)

        books = shelf.library
        
        writeMe = shelf.__str__()
        # open(<filename>, <mode>)
        saveFile = open('MasterLedger.txt', 'w')
        # writes the text contained in the variable writeMe to the file declared above
        saveFile.write(writeMe)
        # Always remember after an operation is completed to close it.
        saveFile.close()

        return render_template('index.html', books=books,  username=session['username'])
    else:
        return redirect(url_for('login'))


# Takes isbn and will make the request for the book
@app.route('/request', methods=['GET', 'POST'])
def request_class():
    if request.method == 'GET':
        isbn = request.args.get('book')
        user = User.query.filter_by(username=session['username']).first()
        shelf.newRequest(isbn, user)
        shelf.createMessage(isbn, 'username', 'owner')
        message = "Your request for" + isbn + "has been successful!"
        return render_template('usermessage.html', username=session['username'], message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():

    """POST runs when a username and password is entered"""
    if request.method == 'POST':
        """Runs if a username has been entered"""
        if request.form['username']:

            session['username'] = request.form['username']

            # CREATES NEW USER OBJECT
            new_user = User(
                username=request.form['username'], password=request.form['password'])

            # IF PASSWORD IS INVALID WARNS USER TO TYPE A VALID PASSWORD.
            if not p.password_valid(request.form['password']):
                message = "use a valid password. They must be 5 - 32 characters long"
                return render_template('login.html', message=message)
            # steps: 1. does user exist
         #       if yes then authorize password
         #       else create user """"

            # CHECK IS USER EXISTS. NOT UNIQUE IF IT IS IN THE DB
            if new_user.exists():  # RUNS IF USER EXISTS
                new_user.print_table()
                if new_user.password_verify():
                    if new_user.getUsername() == 'Regulator':
                        return redirect(url_for('regulator'))
                    else:
                        return redirect(url_for('index'))
                else:
                    message = "check your password. Wrong password was entered"
                    return render_template('login.html', message=message)

                # Authenticate password ( compare db and given )
                # set authenticated to true if same otherwise set to false
            else:
                print("Username does not exist")
                new_user.print_table()
                new_user.insert()

            return redirect(url_for('index'))
        else:
            print('No username')
            message = "input a username"
            return render_template('login.html', message=message)
    else:

        message = "sign in"
        return render_template('login.html', message=message)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.clear()
        # Add db code
        return redirect(url_for('login'))


# USER FUNCTIONS
@app.route('/return-files/')
def download_files():
    user = User.query.filter_by(username=session['username']).first()
    return render_template('requests.html', username = session['username'], message = user.showRequests())

# ADMIN FUNCTIONS
@app.route('/protected')
def regulator():
    return render_template('admin.html')


@app.route('/verify/')
def verify_transactions():
    return 'V T'


@app.route('/view_transactions/')
def display_transactions():
    return 'D T'


@app.route('/display_ledger/')
def display_ledger():
    return 'D ledger'


@app.route('/publish_ledger/')
def publish_ledger():
    return 'P Ledger'


@app.route('/view_users/')
def view_users():`
	return 'View Users'


@app.route('/profile')
def profile():
    return 'Profile'
