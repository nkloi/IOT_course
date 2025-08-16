from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib import messages
from .models import Room, Device, SensorData, LightStatus


def home(request):
    """Home page view"""
    rooms = Room.objects.all()
    devices = Device.objects.all()
    recent_data = SensorData.objects.all()[:10]

    context = {
        'rooms': rooms,
        'devices': devices,
        'recent_data': recent_data,
    }
    return render(request, 'myapp/home.html', context)


class RoomListView(ListView):
    """List all rooms"""
    model = Room
    template_name = 'myapp/room_list.html'
    context_object_name = 'rooms'


class DeviceListView(ListView):
    """List all devices"""
    model = Device
    template_name = 'myapp/device_list.html'
    context_object_name = 'devices'


class SensorDataListView(ListView):
    """List sensor data"""
    model = SensorData
    template_name = 'myapp/sensor_data_list.html'
    context_object_name = 'sensor_data'
    ordering = ['-timestamp']
    paginate_by = 20


def device_status_api(request):
    """API endpoint for device status"""
    devices = Device.objects.all()
    data = []
    for device in devices:
        data.append({
            'id': device.id,
            'name': device.name,
            'device_id': device.device_id,
            'room': device.room.name,
            'status': device.status,
        })
    return JsonResponse({'devices': data})


def sensor_data_api(request):
    """API endpoint for latest sensor data"""
    sensor_data = SensorData.objects.all()[:50]
    data = []
    for item in sensor_data:
        data.append({
            'device': item.device.name,
            'sensor_type': item.sensor_type,
            'value': item.value,
            'unit': item.unit,
            'timestamp': item.timestamp.isoformat(),
        })
    return JsonResponse({'sensor_data': data})


class LightStatusListView(ListView):
    """List all lights with their status"""
    model = LightStatus
    template_name = 'myapp/light_list.html'
    context_object_name = 'lights'


def toggle_light(request, light_id):
    """Toggle light on/off"""
    light = get_object_or_404(LightStatus, id=light_id)
    old_status = "ON" if light.is_on else "OFF"
    light.toggle()
    new_status = "ON" if light.is_on else "OFF"

    messages.success(request, f'{light.device.name} switched from {old_status} to {new_status}')
    return redirect('myapp:light_list')


def light_control_api(request, light_id):
    """API endpoint for light control"""
    light = get_object_or_404(LightStatus, id=light_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'toggle':
            old_status = light.is_on
            light.toggle()
            return JsonResponse({
                'success': True,
                'device': light.device.name,
                'previous_status': old_status,
                'current_status': light.is_on,
                'message': f'Light {"turned on" if light.is_on else "turned off"}'
            })
        elif action == 'on':
            light.is_on = True
            light.save()
            return JsonResponse({'success': True, 'status': 'on'})
        elif action == 'off':
            light.is_on = False
            light.save()
            return JsonResponse({'success': True, 'status': 'off'})

    # GET request - return current status
    return JsonResponse({
        'device': light.device.name,
        'device_id': light.device.device_id,
        'room': light.device.room.name,
        'is_on': light.is_on,
        'last_updated': light.last_updated.isoformat(),
    })


def lights_api(request):
    """API endpoint for all lights status"""
    lights = LightStatus.objects.all()
    data = []
    for light in lights:
        data.append({
            'id': light.id,
            'device': light.device.name,
            'device_id': light.device.device_id,
            'room': light.device.room.name,
            'is_on': light.is_on,
            'last_updated': light.last_updated.isoformat(),
        })
    return JsonResponse({'lights': data})
