class Database:
    def __init__(self):
        self.data = "Dados do Usuário"

    def getData(self):
        return self.data

class Database2:
    def __init__(self) -> None:
        self.data="Novo Banco de Dados"
    def getData(self) -> str:
        return self.data

class IDataRetriever:
    def getData(self):
        pass

class User:
    def __init__(self, dataRetriever: IDataRetriever):
        self.dataRetriever = dataRetriever

    def getUserData(self) -> str:
        return self.dataRetriever.getData()

class Application:
    def __init__(self):
        self.db = Database2()
        self.user = User(self.db)

    def displayUserData(self) -> None:
        print(self.user.getUserData())

# Usage
app = Application()
app.displayUserData()
