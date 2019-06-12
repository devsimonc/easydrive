from PiMotor import Sensor
import time
go = "true"

while go=="true":
    us = Sensor("ULTRASONIC", 15)
    us.trigger()
    if us.Triggered:
        print("Bremsen")
