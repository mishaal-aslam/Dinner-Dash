
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from .category import Category


class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2, validators=[MinValueValidator(1)])
    image = models.ImageField(
        upload_to='uploads/items/', default='standin-photos/items/stand-in-items.jpeg', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Items"
