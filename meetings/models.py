from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.CharField(max_length=20)
    room_no = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.name}: Room {self.room_no}  on  Floor {self.floor}"




class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


