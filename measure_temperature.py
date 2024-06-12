from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
import time, sys
from datetime import datetime

class Sensor:

    def __init__(self, serial=None, hubport=None, timeout=1000, channel=None):
        self.temperature_sensor = TemperatureSensor()
        self.serial  = serial 
        self.hubport = hubport 
        self.timeout = timeout 
        self.channel = channel
        self.temperature_sensor.setHubPort(self.hubport)
        self.temperature_sensor.setDeviceSerialNumber(self.serial)
        self.temperature_sensor.openWaitForAttachment(self.timeout)
        self.temperature_sensor.setChannel(self.channel)

    def read(self):
        return self.temperature_sensor.getTemperature()

    def close(self):
        return self.temperature_sensor.close()


def main():

    if len(sys.argv) < 2:
        print("Specify run number. Example: python measure_temperature.py 10")
        sys.exit(1)
  
    run_number = int(sys.argv[1])
    temperatureSensor0 = Sensor(serial=620013, hubport=0, channel=0)
    temperatureSensor1 = Sensor(serial=620013, hubport=1, channel=0)

    with open(f"./temp_info_{run_number:04d}.csv", "a+") as file:
        file.write(f" Time, Room Temperature (C), Probe Temperature (C)\n")

    read = True
    while read == True:
        current_time = datetime.now()
        probe = temperatureSensor0.read()
        room  = temperatureSensor1.read()

        time_string = current_time.strftime("%H:%M:%S")
        print(f"{time_string}. Room: {room} C. Probe: {probe} C")
        
        with open(f"./data/temp_info_{run_number:04d}.csv", "a+") as file:
            file.write(f"{time_string}, {room}, {probe}\n")

        with open(f"./live_plot.csv", "a+") as file:
            file.write(f"{time_string}, {room}, {probe}\n")

        time.sleep(1)


main()
