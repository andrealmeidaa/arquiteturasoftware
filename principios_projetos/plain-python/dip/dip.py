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