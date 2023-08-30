
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class Customer(models.Model):
    name = models.CharField(max_length=150)
    display_name = models.CharField(
        max_length=32, null=True, blank=True, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name
