from django.core.mail import send_mail

class EmailService:
    @staticmethod
    def send_welcome_email(email,subject,message):
        send_mail(
            subject,
            message,
            'from@example.com',
            [email],
            fail_silently=False,
        )

class LoggerService:
    @staticmethod
    def log_new_user(user):
        logger = logging.getLogger(__name__)
        logger.info(f"New user created: {user.username}")