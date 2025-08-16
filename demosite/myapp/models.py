from django.db import models
from django.utils import timezone

class Room(models.Model):
    """Model for room management"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Device(models.Model):
    """Model for IoT device management"""
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=50, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')
    created_at = models.DateTimeField(auto_now_add=True)


class SensorData(models.Model):
    """Model for sensor data management"""
    SENSOR_TYPES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('light', 'Light'),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    value = models.FloatField()
    unit = models.CharField(max_length=10, default="")
    timestamp = models.DateTimeField(default=timezone.now)


class LightStatus(models.Model):
    """Model for simple light on/off control"""
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    is_on = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def toggle(self):
        """Toggle light on/off"""
        self.is_on = not self.is_on
        self.save()
        return self.is_on
