from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    class Meta:
        db_table='login'
    def __str__(self):
        return self.username
