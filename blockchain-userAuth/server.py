from flask import Flask, render_template, request,url_for,session,redirect
#from . import create_app
import bookshelf
import Book
from user import User, app, db
import password as p

import os
#app= Flask(__name__)
#app=create_app()
db.create_all()
app.secret_key = os.urandom(16)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
        if 'username' in session:

                # shelf=Bookshelf()
        
                book1 = Book.Book('To Kill A Mockingbird', ['Harper Lee'], [
                        'Novel', 'Bildungsroman', 'Southern Gothic', 'Thriller', 'Domestic Fiction', 'Legal Story'], '978-0446310789', 'B0000000001')
                book2 = Book.Book('The Talisman', ['Stephen King', 'Peter Straub'], [
                        'Fantasy', 'Thriller'], '978-1451697216', 'B0000000002')
                book3 = Book.Book('The Bad President', ['Donald Trump'], [
                        'Impeachment', 'Delusional'], '978-1sdfasdfasdff', 'B0000000003')

                shelf=bookshelf.Bookshelf()

                #Adds a Book into the shelf
                shelf.addBook(book1)
                shelf.addBook(book2)
                shelf.addBook(book3)
                 # print(shelf.index[book.getISBN()])

                books=shelf.index

                #Prints every book inside index. 
                """for isbn in books:
                        print(isbn)
                        print(books[isbn].getAuthor())"""

        
                #print(book.getISBN())
                #print("Hello terminal test")
                return render_template('index.html', books= books,  username= session['username'])
        else:
        
                return redirect(url_for('login'))  
#Takes isbn and will make the request for the book
@app.route('/request', methods=['GET', 'POST'])
def request_class():
        if request.method =='GET':
                isbn = request.args.get('book')
                print(isbn)
                return isbn 

@app.route('/login', methods=['GET', 'POST'])
def login():
        """POST runs when a username and password is entered"""
        if request.method=='POST':
                
                """Runs if a username has been entered"""
                if request.form['username']:

                        session['username'] = request.form['username']
                       
                        #CREATES NEW USER OBJECT
                        new_user = User(username=request.form['username'],password =request.form['password'])
                        
                        #IF PASSWORD IS INVALID WARNS USER TO TYPE A VALID PASSWORD.
                        if not p.password_valid(request.form['password']):
                                message="use a valid password. They must be 5 - 32 characters long"
                                return render_template('login.html',message=message) 
                        #steps: 1. does user exist
                         #       if yes then authorize password
                         #       else create user """"

                        #CHECK IS USER EXISTS. NOT UNIQUE IF IT IS IN THE DB

                        if new_user.exists(): #RUNS IF USER EXISTS
                                
                                new_user.print_table()

                                if new_user.password_verify():
                                        return redirect(url_for('index'))  
                                else:
                                        message=" check your password. Wrong password was entered"
                                        return render_template('login.html',message=message)
                                
                                #Authenticate password ( compare db and given )
                                #set authenticated to true if same otherwise set to false
                        else:
                                print("Username does not exist")
                                new_user.print_table()
                                new_user.insert()
                        
                                
                        return redirect(url_for('index'))  
                else:
                        print('No username')
                        message="input a username"
                        return render_template('login.html',message=message) 
        else:
                
                message="sign in"
                return render_template('login.html',message=message)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
        if request.method=='GET':
                session.clear()
                #Add db code
                return redirect(url_for('login')) 
        

@app.route('/profile')
def profile():
        return 'Profile'