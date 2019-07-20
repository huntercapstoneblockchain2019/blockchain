import hashlib,os
 
def hash_password(password):
        #print("hashed_password")
        salt='5gz'
        db_store=password+salt
        hashed_password=hashlib.md5(db_store.encode())
       # print(hashed_password.hexdigest())
        
        return hashed_password.hexdigest()


def password_valid(password):
        #print("password validity")
        """ Minimum 8 and Maximum 32 for password"""

        if not password:
                return False
        elif len(password)>=5 and len(password)<=32:
                return True
        else:
                return False

