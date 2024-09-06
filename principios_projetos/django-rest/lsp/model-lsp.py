class User(models.Model):
    username = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def is_active(self):
        return True

class VerifiedUser(User):
    def is_active(self):
        # The is_active method in VerifiedUser now respects the behavior of User's is_active
        return super().is_active() and self.is_verified