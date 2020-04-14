from django.db import models


# Create your models here.
class holiday(models.Model):
    day = models.CharField(max_length=100)
    date = models.DateField()
    holiday_name = models.CharField(max_length=100)
    holiday_type = models.CharField(max_length=100)
    comment = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.holiday_name
