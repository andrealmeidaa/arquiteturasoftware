# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
import logging

class UserAPIView(APIView):
    def post(self, request):
        # Create a new user
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email']
        )

        # Send a welcome email
        send_mail(
            'Welcome!',
            'Thank you for signing up.',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        # Log the user creation
        logger = logging.getLogger(__name__)
        logger.info(f"New user created: {user.username}")

        return Response({'id': user.id, 'username': user.username})
