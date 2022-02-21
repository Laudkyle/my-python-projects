import psutil, os, subprocess
def battery_status():
    battery = psutil.sensors_battery()
    plugged_in_status = battery.power_plugged
    if plugged_in_status == False:
        charging_status = "No its not!!!"
    elif plugged_in_status:
        charging_status = "Yes it is!!!"
    return charging_status

def cpu_percentage():
    cpu_percentage = psutil.cpu_percent(interval=1)
    return cpu_percentage
def ram_percentage():
    ram_percentage = psutil.virtual_memory().percent
    return ram_percentage
def disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    return disk_usage
