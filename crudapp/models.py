from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=15)
    emis_no = models.CharField(max_length=20)
    aadhaar_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name

