from django.db import models
from django.contrib.auth.models import User


class medical_details(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    medical_check_type = models.CharField(max_length=100)
    Total_Cost = models.FloatField(max_length=100, default='0.0')
    attached_receipt = models.FileField(upload_to='medical_cost/PDF')
    date_you_see_the_doctor = models.DateField()
    year = models.CharField(max_length=100)
    I_hereby_declare_that_all_the_information_provided_above_is_true = models.BooleanField(default=True, null=False)
    recom = (
        ('Review', 'Review'),
        ('Processed', 'Precessed'),

    )
    Status = models.CharField(max_length=100, choices=recom, default='Review')
    process_date = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name


class medical_entitlement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    annual_entitlement = models.FloatField()

    def __str__(self):
        return self.user.first_name
