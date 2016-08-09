import ControlSystems.py
import RPi.GPIO as GPIO

class vehicle:

    def __init__(self, m0a, m0b, m1a, m1b, m2a, m2b, m3a, m3b, m4a, m4b, s):
# Provide GPIO pin values for all the vehicle's motors and the Servo
# 'm1a' is the forward logic output for motor 1 and 'm1b' is reverse.
# m2 is motor 2 and so on.
# 's' is the logic output to control the servo.
# m5 is the grabber arm motor


#       FRONT
#    m0 _____ m2
#     |      |
#     |  m4  |
#     |  s   |
#   m1 ______ m3

        leftMotors = [ Motor(m0a,m0b), Motor(m1a,m1b) ]
        rightMotors = [ Motor(m2a,m2b), Motor(m3a,m3b) ]

        leftSpeed = 0
        rightSpeed = 0

        armMotor = Motor(m4a,m4b)
        servo = Servo(s)


    def __init__(self):
# For a vehicle with a different motor/servo config

        driveMotors = []
        otherMotors = []
        servos = []


    def goStraight(self, speed):

        leftSpeed = speed
        rightSpeed = speed
        for i in range(2):
            self.leftMotors[i].drive(speed)
            self.rightMotors[i].drive(speed)


    def stationaryPivot(self, speed):
# Speed should be between -100 and 100 where negative indicates anti-clockwise
# rotation

        leftSpeed = speed
        rightSpeed = -speed

        for i in range(2):
            self.leftMotors[i].drive(leftSpeed)
            self.rightMotors[i].drive(rightSpeed)


    def modTurnArc(self, extent):
# Creates a difference in power between left and right motors, extent is from
# -100 to 100, negative will cause a left turn, and positave right


        leftSpeed = leftSpeed + extent
        rightSpeed = rightSpeed - extent


        if leftSpeed > 100:
            rightSpeed = rightSpeed - leftSpeed + 100
            leftSpeed = 100

            print leftSpeed
            print rightSpeed

        if leftSpeed < -100:
            rightSpeed = rightSpeed - leftSpeed - 100
            leftSpeed = -100

            print leftSpeed
            print rightSpeed

        if rightSpeed > 100:
            leftSpeed = leftSpeed - rightSpeed + 100
            rightSpeed = 100

            print leftSpeed
            print rightSpeed

        if rightSpeed < -100:
            leftSpeed = leftSpeed - rightSpeed - 100
            rightSpeed = -100

            print leftSpeed
            print rightSpeed

        for i in range(2):
            self.leftMotors[i].drive(leftSpeed)
            self.rightMotors[i].drive(rightSpeed)


    def kill(self):

        self.leftSpeed = 0
        self.rightSpeed = 0
        for i in range(2):
            self.leftMotors[i].drive(leftSpeed)
            self.rightMotors[i].drive(rightSpeed)
