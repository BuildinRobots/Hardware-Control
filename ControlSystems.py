import RPi.GPIO as GPIO

class Motor:
### GPIO.setmode(GPIO.BCM) must be called prior to this class being used ###

    def __init__(self, fwdPin, revPin):
# When initialted, provide pin numbers for forward and reverse logic on GPIO

        GPIO.setup(fwdPin, GPIO.OUT)
        GPIO.setup(revPin, GPIO.OUT)
        self.fwd = GPIO.PWM(fwdPin, 50) # sets pins to 50Hz
        self.rev = GPIO.PWM(revPin, 50) #


    def forward(self, speed):
# Drives Motor forward at a given speed between 1 and 100 until Motor.stop()
# is called
        if speed >= 1 and speed <= 100:
            self.fwd.start(speed)
            return "SUCESS"
        else:
            print "\nInvalid speed, must be between 1-100!"
            return "FAIL"


    def reverse(self, speed):
# Drives Motor backward at a given speed between 1 and 100 until Motor.stop()
# is called
        if speed >= 1 and speed <= 100:
            self.rev.start(speed)
            return "SUCESS"
        else:
            print "\nInvalid speed, must be between 1-100!"
            return "FAIL"


    def stop(self):
# Stops the Motor
        self.fwd.stop()
        self.rev.stop()


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
