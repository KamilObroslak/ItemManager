from django.db import models

class ClientProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class MerchantProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    business_name = models.CharField(max_length=50)  # Przykładowe pole

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) - {self.business_name}"
