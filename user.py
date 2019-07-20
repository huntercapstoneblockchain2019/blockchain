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
            
        

    def exist(self):
        #print("Username used to compare " + self.username)
        user = User.query.filter_by(username=self.username).first()
        #print("User inside func " + str(user))
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

    #def is_anonymous(self: (optional)
        #Returns if user anonymous
    
    #def print_table(self):
        #query=select('*').select_from(db)
        #result=session.execute(query).fetchall()
       # query= session.query(User)
        
        #for m in query:
          #  print(m)

    #checks if username exists in database
   # def is_unique(self): 

        
    
    
   


        