from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultAdmin
from .models import User


@admin.register(User)
class UserAdmin(DefaultAdmin):
    pass
