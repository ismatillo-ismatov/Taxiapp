import uuid
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from driver.models import Driver



class User(AbstractUser):
    pass


class Trip(models.Model):
    REQUESTED = 'REQUESTED'
    STARTED = 'STARTED'
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    STATUSES = (
        (REQUESTED,REQUESTED),
        (STARTED,STARTED),
        (IN_PROGRESS,IN_PROGRESS),
        (COMPLETED,COMPLETED)
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    pick_up = models.CharField(max_length=255)
    drop_off_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=STATUSES,default=REQUESTED)

    def __str__(self):
        return f'{self.id}'


