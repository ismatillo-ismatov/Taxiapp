from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultAdmin
from .models import User, Trip


@admin.register(User)
class UserAdmin(DefaultAdmin):
    pass

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    fields = (
        'id','user','pick_up','drop_off_address','status','created','update',
    )
    list_display = (
        'id','user','pick_up','drop_off_address','status','created','update',
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id','created','update',
    )

