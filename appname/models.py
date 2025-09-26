from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')


class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', "Високий"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='Без коментаря')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.title}"
