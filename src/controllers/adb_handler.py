import subprocess 
import os 
import time

import os

PATH_TO_ADB = "./adb/adb.exe"


class AndroidDevice:
    def __init__(self, adb_path):
        self.adb_path = adb_path
        
    def list_devices(self):
        output = subprocess.run([self.adb_path, "devices"], stdout=subprocess.PIPE)
        devices = []
        for line in output.stdout.decode().split('\n'):
            if 'device' in line and 'List of devices' not in line:
                devices.append(line.split('\t')[0])
        return devices
    
    def connect(self, device_id):
        subprocess.run([self.adb_path, "-s", device_id, "shell"])
        
    def get_device_name(self, device_id):
        output = subprocess.run([self.adb_path, "-s", device_id, "shell", "getprop", "ro.product.model"], stdout=subprocess.PIPE)
        return output.stdout.decode().strip()

    def pull_file(self, device_id, remote_path, local_path):
        timestamp = time.strftime("%Y%m%d-%H%M%S") 
        filename = "generated-readings-{}.xlsx".format(timestamp)
        local_file_path = os.path.join(local_path, filename)
        subprocess.run([self.adb_path, "-s", device_id, "pull", remote_path, local_file_path])
        
    def push_file(self, device_id, local_path, remote_path): 
        subprocess.run([self.adb_path, "-s", device_id, "push", local_path, remote_path])
        
if __name__ == "__main__": 
    # try:
        android = AndroidDevice(PATH_TO_ADB)
        devices = android.list_devices()
        print(devices)
        # device_id = devices[0]
        # android.connect(device_id)
        # name = android.get_device_name(device_id)
        # print(name)
        # android.pull_file(device_id, "/sdcard/Download/generated-readings.xlsx", "C:/Users/Documents/")
        # android.push_file(device_id, "C:/Users/Documents/reading.xlsx")
    # except Exception as e:
    #     print(f"Exception : {e}")