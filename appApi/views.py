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

def updatetemp(request,temp):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    devicestatus.temp = float(temp)
    devicestatus.save()
    return HttpResponse(str(temp))

def updatehumid(request,humid):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    devicestatus.humid = float(humid)
    devicestatus.save()
    return HttpResponse(str(humid))

def updatemoist(request,moist):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    devicestatus.moist = float(moist)
    devicestatus.save()
    return HttpResponse(str(moist))

def toggleswitch(request):
    devicestatus = DeviceStatus.objects.get(device_id='d000')
    if devicestatus.switch==0:
        devicestatus.switch=1
    else:
        devicestatus.switch=0
    devicestatus.save()
    return HttpResponse(str(devicestatus.switch))