class NotificationChannel:
    def send(self, message):
        pass

class EmailNotification(NotificationChannel):
    def send(self, message):
        print(f"Enviando email: {message}")

class SMSNotification(NotificationChannel):
    def send(self, message):
        print(f"Enviando SMS: {message}")

class Notification:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def send(self, message):
        self.channel.send(message)

if __name__=='__main__':
    notificadorEmail=Notification(EmailNotification())
    notificadorEmail.send(message='Uma mensagem')
    notificadorSMS=Notification(SMSNotification())
    notificadorSMS.send(message='Nova mensagem')