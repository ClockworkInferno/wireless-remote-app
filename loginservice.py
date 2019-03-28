from loginrepo import LoginRepo
from user import User

class LoginService:
    def __init__(self,repository):
        self.repository = repository

    def login_user(self, username, password):
        login = self.repository.find(username, password)
        
        return login







