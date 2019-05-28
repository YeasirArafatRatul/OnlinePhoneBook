from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255, unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField()
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images', blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=(
        ('1', 'Male'), ('2', 'Female'), ('3', 'Others')
    ))
    group = models.CharField(max_length=1, blank=True, choices=(
        ('1', 'Family'),
        ('2', 'Friends'),
        ('3', 'Collegue'),
        ('4', 'Neighbours'),
        ('5', 'Relative')
    ))
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-details', kwargs={"pk": self.pk})
