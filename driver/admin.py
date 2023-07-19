from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultAdmin
from .models import Driver


admin.site.register(Driver)