from django.db import models

class TimeSlot(models.Model):

    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES) 
    start_time = models.TimeField()
    stop_time = models.TimeField()
    ids = models.JSONField()  

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.stop_time}"
