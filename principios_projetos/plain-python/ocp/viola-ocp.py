class Notification:
    def send(self, message, channel):
        if channel == 'email':
            print(f"Enviando email: {message}")
        elif channel == 'sms':
            print(f"Enviando SMS: {message}")
        elif channel=='telegram':
            print(f"Enviando Telegram: {message}")
        else:
            raise ValueError("Unknown channel")

if __name__=='__main__':
    notificador=Notification()
    notificador.send(message='Uma mensagem',channel='email')
    notificador.send(message='Nova Mensagem',channel='sms')