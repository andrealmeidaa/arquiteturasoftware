# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class UserAPIView(APIView):
    def get_permissions(self):
        # This method violates the Open/Closed Principle because
        # it has to be modified every time a new user type is added.
        if self.request.user.type == 'admin':
            return [AdminPermission()]
        elif self.request.user.type == 'regular':
            return [RegularUserPermission()]
        elif self.request.user.type=='special':
            return [SpecialUserPermission()]
        # Imagine more elif statements for each new user type.
