from rest_framework.views import APIView
from .permissions import PermissionFactory

class UserAPIView(APIView):
    def get_permissions(self):
        # Now the method is closed for modification but open for extension.
        user_type = self.request.user.type
        return PermissionFactory.get_permissions(user_type)