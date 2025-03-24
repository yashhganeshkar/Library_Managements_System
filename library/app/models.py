from django.db import models
from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    publish_date = models.DateField(null=True, blank=True)
    added_by = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    