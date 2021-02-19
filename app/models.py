from django.db import models

class UserModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()