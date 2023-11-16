from rest_framework.views import APIView
from rest_framework.response import Response
from services import EmailService, LoggerService

class UserAPIView(APIView):
    def post(self, request):
        # Create a new user
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email']
        )

        # Send a welcome email
        EmailService.send_welcome_email(user.email)

        # Log the user creation
        LoggerService.log_new_user(user)

        return Response({'id': user.id, 'username': user.username})