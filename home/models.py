from django.db import models

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=70, null=False)
    last_name = models.CharField(max_length=70, null=False)
    email = models.EmailField(max_length = 254, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return f"{self.email}"