from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


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


class Customer(models.Model):
    name = models.CharField(max_length=150)
    display_name = models.CharField(
        max_length=32, null=True, blank=True, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name
