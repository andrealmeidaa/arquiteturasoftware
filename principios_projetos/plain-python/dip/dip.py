''''
Princípio da Inversão de Dependência (DIP)

O Princípio da Inversão de Dependência (DIP) é um dos cinco princípios SOLID. Nesse princípio, a ideia é que módulos de alto nível não d
evem depender de módulos de baixo nível. 
Ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes. 
Detalhes devem depender de abstrações.

No código abaixo, diferentemente do que foi feito em viola-dip.py, a classe Application 
não depende mais diretamente da classe Logger. Agora a classe Application depende de 
uma abstração Logger, que pode então ser implementada por diferentes classes concretas, 
que nesse exemplo são as classes ConsoleLogger e FileLogger.
'''

class Logger:
    def log(self, mensagem):
        pass

class ConsoleLogger(Logger):
    def log(self, mensagem):
        print(f"Log no console: {mensagem}")

class FileLogger(Logger):
    def log(self, mensagem):
        with open("log.txt", "a") as file:
            file.write(mensagem + "\n")

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log("Applicação está rodando")

if __name__ == "__main__":
    
    app = Application(FileLogger())
    app.run()

    #file_logger = FileLogger()
    #app = Application(file_logger)
    #app.run()