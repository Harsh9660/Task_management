from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='categories')
    assigned_to = models.ManyToManyField(CustomUser, related_name='assigned_categories')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)
    status = models.CharField(max_length=20)
    description = models.TextField()
    organizer = models.ForeignKey(CustomUser, related_name='organized_categories', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks_created')
    assigned_to = models.ForeignKey(CustomUser, related_name='tasks_assigned', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name