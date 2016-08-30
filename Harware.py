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

        self.leftMotors = [ Motor(m0a,m0b), Motor(m1a,m1b) ]
        self.rightMotors = [ Motor(m2a,m2b), Motor(m3a,m3b) ]

        self.leftSpeed = 0
        self.rightSpeed = 0

#        armMotor = Motor(m4a,m4b)
#        servo = servo(s)




    def goStraight(self, speed):

        self.leftSpeed = speed
        self.rightSpeed = speed
        for i in range(2):
            self.leftMotors[i].drive(speed)
            self.rightMotors[i].drive(speed)


    def stationaryPivot(self, speed):
# Speed should be between -100 and 100 where negative indicates anti-clockwise
# rotation

        self.leftSpeed = speed
        self.rightSpeed = -speed

        for i in range(2):
            self.leftMotors[i].drive(self.leftSpeed)
            self.rightMotors[i].drive(self.rightSpeed)


    def modTurnArc(self, extent):
# Creates a difference in power between left and right motors, extent is from
# -100 to 100, negative will cause a left turn, and positave right


        self.leftSpeed = self.leftSpeed + extent
        self.rightSpeed = self.rightSpeed - extent


        if self.leftSpeed > 100:
            self.rightSpeed = self.rightSpeed - self.leftSpeed + 100
            self.leftSpeed = 100

        if self.leftSpeed < -100:
            self.rightSpeed = self.rightSpeed - self.leftSpeed - 100
            self.leftSpeed = -100

        if self.rightSpeed > 100:
            self.leftSpeed = self.leftSpeed - self.rightSpeed + 100
            self.rightSpeed = 100

        if self.rightSpeed < -100:
            self.leftSpeed = self.leftSpeed - self.rightSpeed - 100
            self.rightSpeed = -100


        for i in range(2):
            self.leftMotors[i].drive(self.leftSpeed)
            self.rightMotors[i].drive(self.rightSpeed)


    def kill(self):

        self.leftSpeed = 0
        self.rightSpeed = 0
        for i in range(2):
            self.leftMotors[i].drive(self.leftSpeed)
            self.rightMotors[i].drive(self.rightSpeed)

class Motor:
### GPIO.setmode(GPIO.BCM) must be called prior to this class being used ###

    def __init__(self, fwdPin, revPin):
# When initialted, provide pin numbers for forward and reverse logic on GPIO

        GPIO.setup(fwdPin, GPIO.OUT)
        GPIO.setup(revPin, GPIO.OUT)
        self.fwd = GPIO.PWM(fwdPin, 1) # sets pins to 50Hz
        self.rev = GPIO.PWM(revPin, 1) #
        self.fwd.start(0)
        self.rev.start(0)

    def drive(self, speed):
# Drives Motor at a given speed between -100 and 100

        if speed > 0 and speed <= 100:
            self.rev.ChangeDutyCycle(0)
            self.fwd.ChangeDutyCycle(speed)
            return "forward"

        elif speed < 0 and speed >= -100:
            self.fwd.ChangeDutyCycle(0)
            self.rev.ChangeDutyCycle(-speed)
            return "reverse"

        elif speed is 0:
            self.fwd.ChangeDutyCycle(0)
            self.rev.ChangeDutyCycle(0)
            return "stop"

        else:
            print "\nERROR: Invalid speed, must be between -100 and 100!"
            return "FAIL"


class servo:
### GPIO.setmode(GPIO.BCM) must be called prior to this class being used ###

        def __init__(self, pin):
# Set GPIO pin to appropriate value for servo control
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, 100) # allocates GPIO pin and frequency
            self.pwm.start(5)   # starts pwm at duty of 5


        def setAngle(self, angle):
# Sets the servo to a given angle
            duty = float(angle) / 10.0 + 2.5
            self.pwm.ChangeDutyCycle(duty)


