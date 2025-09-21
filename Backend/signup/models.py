
# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user_type_choices = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('coordinator', 'Coordinator'),
    ]
    user_type = models.CharField(max_length=20, choices=user_type_choices, default='student')

    def __str__(self):
        return self.username
