from django.db import models

# Create your models here.
class Tasktable(models.Model):
    priority_choice = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    completed_choices = [
        ('no', 'No'),
        ('yes', 'Yes'),
    ]
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    completed = models.CharField(max_length=20, choices=completed_choices, default='no')
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=priority_choice)
    