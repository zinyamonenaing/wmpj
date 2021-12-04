from django.db import models

# Create your models here.
class Clinic(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=255)
    patient_address = models.TextField()
    patient_case = models.TextField()
    fileupload = models.FileField(upload_to='files')
    drug = models.TextField()
    fees = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
    doctor = models.CharField(max_length=255)

    def __str__(self):
        return self.patient_name