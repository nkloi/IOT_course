from django.contrib import admin
from .models import Room, Device, SensorData, LightStatus


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id', 'room', 'status', 'created_at')
    list_filter = ('status', 'room')
    search_fields = ('name', 'device_id')
    readonly_fields = ('created_at',)


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'sensor_type', 'value', 'unit', 'timestamp')
    list_filter = ('sensor_type', 'device__room', 'timestamp')
    search_fields = ('device__name',)
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'


@admin.register(LightStatus)
class LightStatusAdmin(admin.ModelAdmin):
    list_display = ('device', 'is_on', 'last_updated')
    list_filter = ('is_on', 'device__room')
    search_fields = ('device__name', 'device__device_id')
    readonly_fields = ('last_updated',)
    actions = ['turn_on_lights', 'turn_off_lights']

    def turn_on_lights(self, request, queryset):
        updated = queryset.update(is_on=True)
        self.message_user(request, f'{updated} lights turned on.')
    turn_on_lights.short_description = "Turn on selected lights"

    def turn_off_lights(self, request, queryset):
        updated = queryset.update(is_on=False)
        self.message_user(request, f'{updated} lights turned off.')
    turn_off_lights.short_description = "Turn off selected lights"
