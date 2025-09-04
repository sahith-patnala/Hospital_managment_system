from django.db import models
from datetime import datetime

# Create your models here.

class Appointment(models.Model):
    DEPARTMENTS = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('orthopedics', 'Orthopedics'),
        ('pediatrics', 'Pediatrics'),
        ('general', 'General'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=20, choices=DEPARTMENTS)
    date = models.DateField()
    time = models.TimeField()

    def _str_(self):
        return self.name


class data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    
    is_resolved=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='data'
        verbose_name_plural='datas'
    
    def __str__(self):
        return self.email
