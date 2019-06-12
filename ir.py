from PiMotor import Sensor
import time
go = "true"

while go=="true":
    us1 = Sensor("IR1", 1)
    us1.trigger()
    us2 = Sensor("IR2", 1)
    us2.trigger()
    if us1.Triggered and us2.Triggered:
        print("stop")
    elif us1.Triggered:
        print("rechts")
    elif us2.Triggered:
        print("links")
