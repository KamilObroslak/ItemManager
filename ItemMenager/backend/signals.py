from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ClientProfile, MerchantProfile
from django.core.mail import send_mail

@receiver(post_save, sender=ClientProfile or MerchantProfile)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"User created: {instance.first_name} {instance.last_name}")  # Informacja o utworzeniu użytkownika

        send_mail(
            'Welcome!',
            f'Hello {instance.first_name}, welcome to our platform!',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )

        print(f"Email sent to: {instance.email}")  # Informacja o wysłaniu e-maila
