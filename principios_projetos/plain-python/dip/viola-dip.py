class Logger:
    def log(self, mensagem):
        print(f"Registrando mensagem de log: {mensagem}")

class Application:
    def __init__(self):
        self.logger = Logger()

    def run(self):
        self.logger.log("Aplicação está rodando")

if __name__ == "__main__":
    app = Application()
    app.run()
