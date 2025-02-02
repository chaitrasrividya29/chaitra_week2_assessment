from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self,name):
        self.username=name
        print(f"{self.username} has logged into GOOGLE sucessfully")
    def logout(self):
        print(f"{self.username} is logged out from GOOGLE")

class FacebookAuth(UserAuthentication):
    def login(self,name):
        self.username=name
        print(f"{self.username} has logged into FACEBOOK sucessfully")
    def logout(self):
        print(f"{self.username} is logged out from FACEBOOK")
        
def main():
    Google=GoogleAuth()
    Facebook=FacebookAuth()
    Google.login("chaitra")
    Facebook.login("chaitra")
    Google.logout()
    Facebook.logout()

main()