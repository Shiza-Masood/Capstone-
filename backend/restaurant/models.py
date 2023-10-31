from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Booking(models.Model):
    id = models.PositiveIntegerField(primary_key=True,validators=[MaxValueValidator(99999999999)])
    name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField()
    def __str__(self):
        return self.name


class Menu(models.Model):
    unique = models.PositiveIntegerField(primary_key=True,validators=[MaxValueValidator(99999)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    def __str__(self):
        return self.title