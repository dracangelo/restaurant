from django.db import models
from django.utils import timezone
# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_people =  models.IntegerField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name