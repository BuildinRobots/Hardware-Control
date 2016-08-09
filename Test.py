import ControlSystems.py
import Vehicle.py
import RPi.GPIO as GPIO
import time

# Setup the pi's GPIO
GPIO.setmode(GPIO.BCM)
#         m1 ,   m2 ,  m3 ,   m4 ,  m5 , s
vehicle(27,22, 23,24, 6,13, 19,26, 4,17, 12)

print "Driving Forward, speed 100%..."
vehicle.goStraight(100)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Driving Backward, speed 100%..."
vehicle.goStraight(-100)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Driving Forward, speed 50%..."
vehicle.goStraight(50)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Driving Backward, speed 50%..."
vehicle.goStraight(50)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Testing clockwise pivot, speed 75%"
vehicle.stationaryPivot(75)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Testing anti-clockwise pivot, speed 75%"
vehicle.stationaryPivot(-75)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Testing forward arc, extent 20, speed 40%"
vehicle.goStraight(40)
vehicle.modTurnArc(20)
time.sleep(2)
vehicle.kill()
print "done"
time.sleep(0.5)

print "Test over!"
