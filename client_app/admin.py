from django.contrib import admin
from .models import Client, Status, Role, Details

# Register your models here.

admin.site.register(Client)
admin.site.register(Status)
admin.site.register(Role)
admin.site.register(Details)