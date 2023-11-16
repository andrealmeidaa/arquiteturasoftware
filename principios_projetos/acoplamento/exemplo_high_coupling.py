class Database:
    def __init__(self):
        self.data = "User data in database"

    def getData(self):
        return self.data

class User:
    def __init__(self, db: Database):
        self.db = db

    def getUserData(self):
        return self.db.getData()

class Application:
    def __init__(self):
        self.db = Database()
        self.user = User(self.db)

    def displayUserData(self):
        print(self.user.getUserData())

# Usage
app = Application()
app.displayUserData()
