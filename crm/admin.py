from django.contrib import admin
from .models import Client, Task, Interaction

admin.site.register(Client)
admin.site.register(Task)
admin.site.register(Interaction)