# dao.py
class UserDAO:
    def get_user(self, user_id):
        # Logic to retrieve the user from the database
        pass

# email_service.py
class EmailService:
    def send_email(self, email, message):
        # Logic to send email
        pass

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .dao import UserDAO
from .email_service import EmailService

class UserEmailAPIView(APIView):
    def post(self, request, user_id):
        user_dao = UserDAO()
        user = user_dao.get_user(user_id)
        
        email_service = EmailService()
        email_service.send_email(user.email, "Your account has been created.")
        
        return Response({"message": "Email sent to user."})
