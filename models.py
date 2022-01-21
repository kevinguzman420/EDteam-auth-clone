from flask_login import UserMixin

users = []

class User(UserMixin):
    
    def __init__(self, id, username, lastname, email, password):
        self.id = id
        self.username = username
        self.lastname = lastname
        self.email = email
        self.password = password
        
    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return False
            
def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
        
