from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import password as p
#from blockchain import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 

class User(db.Model):
	__tablename__='user'

	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80),unique=True,nullable=False)
	password = db.Column(db.String,nullable=False)
	authenticated = db.Column(db.Boolean,default = False)
	
	__bookrequests={}

	def __init__(self,username,password,authenticated=True):
		self.username=username
		self.password=p.hash_password(password)
		self.authenticated=authenticated #add password verify

	# def newuser(self,username,password,active=True):

	def is_autenticated(self):
		return self.authenticated

	def password_verify(self): #ADD CODE TO CHECK FOR PASSWORD
		# print("password verify")
		user = User.query.filter_by(username=self.username).first()
		#print("DB Password "+user.password+" Object pass "+ self.password)
		if user.password == self.password:
			#set authorized to true
			return True
		else:
			#set authorized to false
			return False

	def exists(self):
		#print("Username used to compare " + self.username)
		user = User.query.filter_by(username=self.username).first()
		#print("User inside func " + str(user))
		#IF NONE NO USER WAS FOUND
		if user is None: 
			return False
		else:
			return True

	def insert(self):
		print("Inserting User")
		print(self.username)
		print(self.password)
		print(self.authenticated)
		db.session.add(self)
		db.session.commit()

	def print_table(self):
		res = User.query.all()
		for m in res:
			print (" ID" + str(m.id) + " Username " + m.username+ " Password "+ m.password + " Authorized "+ str(m.authenticated))


	def clear_table(self):
		db.session.query(User).delete()
		db.session.commit()

	#def is_authenticated (self):
	#check if password is same as stored 

	#def get_id(self):
	#return id of user
	
	#Accessor Function		
	def getUsername(self):
		return self.username

	#Adds a new request to user's dictionary of requests	
	def addBookRequest(self, isbn, rqid):
		if self.activeRequest(isbn) == False:
			self.__bookrequests[isbn] = rqid
			message = "request successfully added"
		else:
			message = "request for book already exist"
		return message		
		
	def showRequests(self):
		message =[]
		for isbn in self.__bookrequests:
			message.append("book:"+ repr(isbn) +"request id: " + repr(self.__bookrequests[isbn]))
		return message
	
	def getRequestId(self, isbn):
		return self.__bookrequests[isbn]

	def activeRequest(self, isbn):
		if isbn in self.__bookrequests:
			return True
		else:
			return False

					
					
	
	#def getBookChain(self, isbn):

	#Given the request id as a parameter and the book's isbn a transaction block 
	# is created and returned by user 
	#def createTransactionBlock(self, req_id, isbn):
		#blk_chain = self.getBookChain(isbn) # get corresponding blockchain for book with isbn
		#prev_blk = blk_chain.last_block()
		#trans_block = block.Block(prev_blk.getBlockHash(), req_id)
		#return trans_block
	














