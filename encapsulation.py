class User :
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def get_username(self):
        return self.__username 
    def verify_password(self,username):
        return self.__password == password


class signup(User):
    def __init__(self):
        self.registerd_id = {}
    def created_account(self,username,password):
        if username in self.registerd_id:
            return "Username already existis"
        if len(password) < 4:
            return "Password should be 4 chatectars more long"

        new_user = User(username,password)
        self.registerd_id[username] = new_user
        return "New acount is created"


class login(signup):
    def authenticate(self , username, password):
     if username not in self.registerd_id:
        return "No id found on such username"

        user = self.registerd_id[username] 
        if user.verify_password(password):
            return f"Wellcome back,{user.get_username()}"
        else:
            "Incorrect password"


if __name__ == "__main__":
    system = login()
    

    while True:
        print("\n Login system")
        print("1. Sign up")
        print("2. Login ")
        print("3. Exit")
    
        choose = input("choose an option ")

        if choose == '1':
            uname = input("Enter username")
            pwd = input("Enter password")
            print(system.created_account(uname,pwd))
        
        elif choose == '2':
            uname = input("Enter username")
            pwd = input("Enter password")
            print(system.authenticate(uname,pwd))

        elif choose == '3':
            print("Exit system")
            break

        else:
            print("Invalid options")

    










