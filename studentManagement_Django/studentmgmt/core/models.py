from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=20, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    totalfees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    feesPaid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.studentName

