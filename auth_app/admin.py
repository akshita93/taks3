from django.contrib import admin
from django.contrib.auth import models
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'first_name', 'last_name', 'email','password']


admin.site.register(User,UserAdmin)