from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)

    def __str__(self):

        return self.title
    
class Interaction(models.Model):
    INTERACKTION_TYPE = (
        ('call', 'Call'),
        ('email', 'Email'),
        ('meeting', 'Meeting')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='Interactions')
    interaction_type = models.CharField(max_length=10, choices=INTERACKTION_TYPE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_interaction_type_display()} с {self.client.name}'
    
    
