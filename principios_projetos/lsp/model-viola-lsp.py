class User(models.Model):
    username = models.CharField(max_length=100)

    def is_active(self):
        return True

class VerifiedUser(User):
    def is_active(self):
        # For a VerifiedUser, is_active depends on an external verification process
        return external_verification_service.is_user_verified(self.username)