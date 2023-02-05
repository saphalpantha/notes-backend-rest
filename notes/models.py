from enum import auto
from turtle import update
from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.body[0:30]

