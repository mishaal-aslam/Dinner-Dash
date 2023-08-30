from django.db import models
from Items.Models.items import Items
from Items.Models.customer import Customer
from django.core.validators import MinValueValidator
import datetime


class Order(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2, validators=[MinValueValidator(1)])
    address = models.CharField(max_length=150, default='')
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title
