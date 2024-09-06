class UserAPIView(APIView):
    def get(self, request, username):
        user = User.objects.get(username=username)
        if user.is_active():
            return Response({"message": "User is active"})
        else:
            return Response({"message": "User is not active"}, status=400)


#Se fosse no get fosse passado uma instância de VerifiedUser, o metódo sobrescrito não deve fazer alterações drásticas no funcionamento da hierarquia.