from django.shortcuts import render,HttpResponse
from .models import DeviceStatus
# Create your views here.
def gettemp(request):
    devicestatus = DeviceStatus.objects.get(device_id='d000') 
    return HttpResponse(str(devicestatus.temp))

def gethumid(request):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    return HttpResponse(str(devicestatus.humid))

def getmoist(request):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    return HttpResponse(str(devicestatus.moist))