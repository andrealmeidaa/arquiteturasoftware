# interfaces.py
from abc import ABC, abstractmethod

#São criadas interfaces para o serviço, que facilita a substituição
class IUserDAO(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

class IEmailService(ABC):
    @abstractmethod
    def send_email(self, email, message):
        pass

# dao.py
from .interfaces import IUserDAO
#Implementações concretas. Novos DAOs e E-mails poderiam ser adicionados sem modificar o comportamente da view
class UserDAO(IUserDAO):
    def get_user(self, user_id):
        # Logic to retrieve the user from the database
        pass

# email_service.py
from .interfaces import IEmailService

class EmailService(IEmailService):
    def send_email(self, email, message):
        # Logic to send email
        pass

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class UserEmailAPIView(APIView):
    def __init__(self, user_dao: IUserDAO, email_service: IEmailService): #As instâncias concretas são passadas no construtor e não mais fixadas dentro da view
        self.user_dao = user_dao
        self.email_service = email_service

    def post(self, request, user_id):
        user = self.user_dao.get_user(user_id)
        self.email_service.send_email(user.email, "Your account has been created.")
        
        return Response({"message": "Email sent to user."})

# Exemplo em alto níve: api-view=UserEmailAPIView(UserDAO(),EmailService())