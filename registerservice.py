from user import User
#from loginrepo import LoginRepo

class RegisterService:
    def __init__(self,repository):
        self.repository = repository
        
    def register_user(self, username, password, email, fname, lname):
        register = self.repository.add(username, password, email, fname, lname)
        return register
class QueryRegister:
    def __init__(self,repository):
        self.repository = repository
    def find(self, username, password, email)
        return RegUser(username, password, email)
