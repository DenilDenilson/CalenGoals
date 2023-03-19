from flask_login import UserMixin

db_user = []

class User(UserMixin):
    def __init__(self, id, alias, password):
        self.id = id
        self.alias = alias
        self.password = password
    
    def verify_password(self, password):
        if self.password == password:
            return True
        return False
def get_user(alias):
    for user in db_user:
        if user.alias == alias:
            return user
        return None