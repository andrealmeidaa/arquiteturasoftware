class User(models.Model):
    username = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def is_active(self):
        return True

class VerifiedUser(User):
    def is_active(self):
        # O método is_active da classe VerifiedUser agora respeita o comportamento definido no método is_active da classe User
        return super().is_active() and self.is_verified