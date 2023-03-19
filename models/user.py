from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

db_user = []

class User(UserMixin):
    def __init__(self, id, alias, password):
        self.id = id
        self.alias = alias
        self.password = generate_password_hash(password)
    
    def verify_password(self, password):
        # if self.password == password:
        #     return True
        # return False
        return check_password_hash(self.password, password)
    
def get_user(alias):
    for user in db_user:
        if user.alias == alias:
            return user
        return None